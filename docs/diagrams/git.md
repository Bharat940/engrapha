# Diagram: Git

Git diagrams visualize branches, commits, and merge commits on horizontal or vertical timelines.

## Minimal example

```python
import engrapha_notes as en
import engrapha_diagrams as ed

git = ed.GitDiagram(
    width=400, height=150, caption="Fig 14: Git Flow"
)

git.commit("main",      "c1: Initial commit")
git.branch("main",      "feature/login")
git.commit("feature",   "c2: Add login form")
git.commit("main",      "c3: Hotfix typo")
git.merge("feature",    "main", "c4: Merge feature/login")

en.add(git.as_flowable())
```

## Commits

```python
git.commit("main", "c1: Initial commit")
```

If `label` is empty, the commit is drawn but unlabeled.

## Branches

```python
git.branch("main", "feature")   # create feature from main
```

Existing branches are tracked automatically; subsequent `branch()` calls with the same child are silently ignored.

## Merges

```python
git.merge("feature", "main", "c4: Merge feature/login")
```

The merge commits a dot on the target branch; the source branch is drawn as a curve back into it.

## Colours

Branch colors are assigned automatically from a palette. Override manually by editing `_branch_colors` on the instance.

## Commit spacing

```python
git = ed.GitDiagram(
    width=400, height=150,
    commit_spacing=65.0,   # pixels between commit points
)
```

## Labels

If two commits land on the same branch consecutively, labels alternate up / down to avoid overlap.

## Next

- [Gallery](../gallery/index.md)
- [Examples](../examples/engineering-notes.md)

