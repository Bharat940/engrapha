"""
layout.py -- Auto-layout helpers for paperforge_diagrams.

These are pure math functions; they never touch reportlab directly.
All positions are in reportlab's coordinate system (origin bottom-left, points).
"""

from __future__ import annotations

import math

# ---------------------------------------------------------------------------
# Grid and row layouts
# ---------------------------------------------------------------------------


def grid_positions(
    count: int,
    cols: int,
    cell_w: float,
    cell_h: float,
    origin_x: float = 0.0,
    origin_y: float = 0.0,
) -> list[tuple[float, float]]:
    """
    Return (x, y) centers for `count` items in a grid with `cols` columns.
    Origin is the bottom-left of the grid. Rows fill top-to-bottom.
    """
    if cols < 1:
        raise ValueError(f"cols must be >= 1, got {cols}")
    positions: list[tuple[float, float]] = []
    rows = math.ceil(count / cols)
    for i in range(count):
        col = i % cols
        row = rows - 1 - (i // cols)  # top row first
        x = origin_x + col * cell_w + cell_w / 2
        y = origin_y + row * cell_h + cell_h / 2
        positions.append((x, y))
    return positions


def row_positions(
    count: int,
    spacing: float,
    origin_x: float = 0.0,
    y: float = 0.0,
) -> list[tuple[float, float]]:
    """Return `count` (x, y) centers evenly spaced along a horizontal row."""
    if count < 1:
        return []
    total_w = spacing * (count - 1)
    start_x = origin_x - total_w / 2
    return [(start_x + i * spacing, y) for i in range(count)]


def column_positions(
    count: int,
    spacing: float,
    x: float = 0.0,
    origin_y: float = 0.0,
) -> list[tuple[float, float]]:
    """Return `count` (x, y) centers evenly spaced along a vertical column."""
    if count < 1:
        return []
    return [(x, origin_y + i * spacing) for i in range(count)]


def distribute_around(
    cx: float,
    cy: float,
    radius: float,
    count: int,
    start_angle_deg: float = 90.0,
) -> list[tuple[float, float]]:
    """
    Place `count` points evenly on a circle of given radius centered at (cx, cy).
    start_angle_deg controls where the first point is placed (default: top).
    """
    if count < 1:
        return []
    step = 360.0 / count
    positions: list[tuple[float, float]] = []
    for i in range(count):
        angle = math.radians(start_angle_deg - i * step)
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        positions.append((x, y))
    return positions


# ---------------------------------------------------------------------------
# Edge routing
# ---------------------------------------------------------------------------


def route_orthogonal(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    prefer: str = "horizontal",
) -> list[tuple[float, float]]:
    """
    Compute waypoints for an L-shaped orthogonal edge between two points.
    Returns a list of (x, y) points including the start and end.
    prefer: 'horizontal' -- exit horizontally first, then vertically
            'vertical'   -- exit vertically first, then horizontally
    """
    if prefer == "horizontal":
        mid_x = (x1 + x2) / 2
        return [(x1, y1), (mid_x, y1), (mid_x, y2), (x2, y2)]
    else:
        mid_y = (y1 + y2) / 2
        return [(x1, y1), (x1, mid_y), (x2, mid_y), (x2, y2)]


def midpoint(x1: float, y1: float, x2: float, y2: float) -> tuple[float, float]:
    """Return the midpoint between two points."""
    return (x1 + x2) / 2, (y1 + y2) / 2


def edge_clip_rect(
    cx: float,
    cy: float,
    w: float,
    h: float,
    tx: float,
    ty: float,
) -> tuple[float, float]:
    """
    Find where the line from (cx, cy) to (tx, ty) exits the rectangle
    centered at (cx, cy) with size (w, h). Returns the exit point on the border.
    Used to clip arrow endpoints to the edge of a node rectangle.
    """
    dx = tx - cx
    dy = ty - cy
    if abs(dx) < 1e-9 and abs(dy) < 1e-9:
        return cx, cy

    hw = w / 2
    hh = h / 2

    # Scale factor to reach each edge
    candidates: list[float] = []
    if abs(dx) > 1e-9:
        t_right = hw / abs(dx)
        t_left = hw / abs(dx)
        candidates.extend([t_right, t_left])
    if abs(dy) > 1e-9:
        t_top = hh / abs(dy)
        t_bot = hh / abs(dy)
        candidates.extend([t_top, t_bot])

    t = min(candidates)
    return cx + dx * t, cy + dy * t


def edge_clip_circle(
    cx: float,
    cy: float,
    r: float,
    tx: float,
    ty: float,
) -> tuple[float, float]:
    """
    Find where the line from (cx, cy) to (tx, ty) exits the circle at (cx, cy).
    """
    dx = tx - cx
    dy = ty - cy
    length = math.hypot(dx, dy)
    if length < 1e-9:
        return cx + r, cy
    return cx + dx / length * r, cy + dy / length * r


def edge_clip_diamond(
    cx: float,
    cy: float,
    w: float,
    h: float,
    tx: float,
    ty: float,
) -> tuple[float, float]:
    """Find where a ray from a diamond's center intersects its border."""
    dx = tx - cx
    dy = ty - cy
    if abs(dx) < 1e-9 and abs(dy) < 1e-9:
        return cx, cy
    scale = 1.0 / (abs(dx) / (w / 2.0) + abs(dy) / (h / 2.0))
    return cx + dx * scale, cy + dy * scale


def bus_line_y(height: float, margin: float = 20.0) -> float:
    """Y coordinate for the shared bus line in a bus topology diagram."""
    return height / 2


def sequence_x_positions(
    count: int,
    diagram_width: float,
    margin: float = 40.0,
) -> list[float]:
    """
    Evenly spaced x positions for sequence diagram lifelines.
    """
    if count < 1:
        return []
    usable = diagram_width - margin * 2
    if count == 1:
        return [diagram_width / 2]
    spacing = usable / (count - 1)
    return [margin + i * spacing for i in range(count)]


def auto_layout_graph(
    node_ids: list[str],
    edges: list[tuple[str, str]],
    width: float,
    height: float,
    margin_x: float = 50.0,
    margin_y: float = 40.0,
    direction: str = "TB",
) -> dict[str, tuple[float, float]]:
    """
    Auto-layouts a directed graph using a Sugiyama-style hierarchical layout with dummy nodes.
    Returns: dict of node_id -> (x, y) coordinates.
    direction: 'TB' (top-to-bottom) or 'LR' (left-to-right).
    """
    if not node_ids:
        return {}

    # 1. Build adjacency list and in-degrees
    adj: dict[str, list[str]] = {nid: [] for nid in node_ids}
    in_degree: dict[str, int] = {nid: 0 for nid in node_ids}
    for u, v in edges:
        if u in adj and v in adj:
            adj[u].append(v)
            in_degree[v] += 1

    # DFS to find back-edges (cycles)
    visited: dict[str, int] = {nid: 0 for nid in node_ids}
    back_edges: set[tuple[str, str]] = set()

    def dfs(u: str) -> None:
        visited[u] = 1  # visiting
        for v in adj[u]:
            if visited.get(v, 0) == 1:
                back_edges.add((u, v))
            elif visited.get(v, 0) == 0:
                dfs(v)
        visited[u] = 2  # visited

    for nid in node_ids:
        if visited[nid] == 0:
            dfs(nid)

    # Build DAG adjacency list by reversing back-edges
    dag_adj: dict[str, list[str]] = {nid: [] for nid in node_ids}
    for u in node_ids:
        for v in adj[u]:
            if (u, v) in back_edges:
                dag_adj[v].append(u)
            else:
                dag_adj[u].append(v)

    # 2. Compute ranks/layers using Bellman-Ford rank propagation on the DAG
    ranks: dict[str, int] = {nid: 0 for nid in node_ids}
    for _ in range(len(node_ids)):
        changed = False
        for u in node_ids:
            for v in dag_adj[u]:
                if ranks[v] <= ranks[u]:
                    ranks[v] = ranks[u] + 1
                    changed = True
        if not changed:
            break

    # 2.5 Insert dummy nodes for long edges to resolve bypass overlaps
    extended_node_ids = list(node_ids)
    extended_layers: dict[int, list[str]] = {}
    for nid, r in ranks.items():
        extended_layers.setdefault(r, []).append(nid)

    dummy_index = 0
    pos_adj: dict[str, list[str]] = {nid: list(dag_adj[nid]) for nid in node_ids}

    for u in list(node_ids):
        for v in list(dag_adj[u]):
            span = ranks[v] - ranks[u]
            if span > 1:
                # Remove v from u's adjacency list in pos_adj
                if v in pos_adj[u]:
                    pos_adj[u].remove(v)
                # Insert a chain of dummy nodes
                prev_node = u
                for r in range(ranks[u] + 1, ranks[v]):
                    dummy_id = f"__dummy_{dummy_index}"
                    dummy_index += 1
                    extended_node_ids.append(dummy_id)
                    extended_layers.setdefault(r, []).append(dummy_id)
                    ranks[dummy_id] = r
                    pos_adj[dummy_id] = []
                    pos_adj[prev_node].append(dummy_id)
                    prev_node = dummy_id
                # Connect the last dummy node to v
                pos_adj[prev_node].append(v)

    # Group nodes by rank
    layers = extended_layers
    sorted_ranks = sorted(layers.keys())
    num_layers = len(sorted_ranks)

    # 3. Position nodes within layers
    positions: dict[str, tuple[float, float]] = {}
    usable_w = width - margin_x * 2.0
    usable_h = height - margin_y * 2.0

    if direction == "TB":
        # Initialize positions for the first layer
        first_rank = sorted_ranks[0] if sorted_ranks else 0
        first_layer_nodes = layers.get(first_rank, [])
        first_layer_nodes.sort()
        
        node_spacing_tb = 140.0
        k = len(first_layer_nodes)
        total_layer_w = (k - 1) * node_spacing_tb
        start_x = width / 2.0 - total_layer_w / 2.0
        
        for idx, nid in enumerate(first_layer_nodes):
            if k > 1 and total_layer_w > usable_w:
                x = margin_x + idx * (usable_w / (k - 1))
            else:
                x = start_x + idx * node_spacing_tb
            y = height - margin_y
            positions[nid] = (x, y)

        # Position subsequent layers
        for r_idx, r in enumerate(sorted_ranks[1:]):
            nodes_in_layer = layers[r]

            # Calculate barycenters (average X of parents in pos_adj)
            barycenters: dict[str, float] = {}
            for nid in nodes_in_layer:
                parents = [p for p in extended_node_ids if p in pos_adj and nid in pos_adj[p] and p in positions]
                if parents:
                    barycenters[nid] = sum(positions[p][0] for p in parents) / len(
                        parents
                    )
                else:
                    barycenters[nid] = width / 2.0

            # Sort nodes by barycenter, then alphabetically to stay deterministic
            nodes_in_layer.sort(key=lambda nid: (barycenters[nid], nid))

            # Space out
            y = height - margin_y - (r_idx + 1) * (usable_h / max(num_layers - 1, 1))
            k = len(nodes_in_layer)
            if k > 1:
                avg_bary = sum(barycenters[nid] for nid in nodes_in_layer) / k
                total_layer_w = (k - 1) * node_spacing_tb
                start_x = avg_bary - total_layer_w / 2.0
                
                if total_layer_w > usable_w:
                    for idx, nid in enumerate(nodes_in_layer):
                        x = margin_x + idx * (usable_w / (k - 1))
                        positions[nid] = (x, y)
                else:
                    if start_x < margin_x:
                        start_x = margin_x
                    elif start_x + total_layer_w > width - margin_x:
                        start_x = width - margin_x - total_layer_w
                    
                    for idx, nid in enumerate(nodes_in_layer):
                        x = start_x + idx * node_spacing_tb
                        positions[nid] = (x, y)
            else:
                nid = nodes_in_layer[0]
                x = max(margin_x, min(width - margin_x, barycenters[nid]))
                positions[nid] = (x, y)

    elif direction == "LR":
        # Initialize positions for the first layer
        first_rank = sorted_ranks[0] if sorted_ranks else 0
        first_layer_nodes = layers.get(first_rank, [])
        first_layer_nodes.sort()
        
        node_spacing_lr = 80.0
        k = len(first_layer_nodes)
        total_layer_h = (k - 1) * node_spacing_lr
        start_y = height / 2.0 + total_layer_h / 2.0
        
        for idx, nid in enumerate(first_layer_nodes):
            if k > 1 and total_layer_h > usable_h:
                y = height - margin_y - idx * (usable_h / (k - 1))
            else:
                y = start_y - idx * node_spacing_lr
            x = margin_x
            positions[nid] = (x, y)

        # Position subsequent layers
        for r_idx, r in enumerate(sorted_ranks[1:]):
            nodes_in_layer = layers[r]

            # Calculate barycenters (average Y of parents in pos_adj)
            barycenters_lr: dict[str, float] = {}
            for nid in nodes_in_layer:
                parents = [p for p in extended_node_ids if p in pos_adj and nid in pos_adj[p] and p in positions]
                if parents:
                    barycenters_lr[nid] = sum(positions[p][1] for p in parents) / len(
                        parents
                    )
                else:
                    barycenters_lr[nid] = height / 2.0

            # Sort nodes by barycenter, then alphabetically to stay deterministic
            nodes_in_layer.sort(key=lambda nid: (barycenters_lr[nid], nid))

            # Space out
            x = margin_x + (r_idx + 1) * (usable_w / max(num_layers - 1, 1))
            k = len(nodes_in_layer)
            if k > 1:
                avg_bary = sum(barycenters_lr[nid] for nid in nodes_in_layer) / k
                total_layer_h = (k - 1) * node_spacing_lr
                start_y = avg_bary + total_layer_h / 2.0
                
                if total_layer_h > usable_h:
                    for idx, nid in enumerate(nodes_in_layer):
                        y = height - margin_y - idx * (usable_h / (k - 1))
                        positions[nid] = (x, y)
                else:
                    if start_y > height - margin_y:
                        start_y = height - margin_y
                    elif start_y - total_layer_h < margin_y:
                        start_y = margin_y + total_layer_h
                    
                    for idx, nid in enumerate(nodes_in_layer):
                        y = start_y - idx * node_spacing_lr
                        positions[nid] = (x, y)
            else:
                nid = nodes_in_layer[0]
                y = max(margin_y, min(height - margin_y, barycenters_lr[nid]))
                positions[nid] = (x, y)

    return {nid: coord for nid, coord in positions.items() if nid in node_ids}
