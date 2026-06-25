"""
React.js & Next.js Fundamentals with Tailwind CSS -- Complete Developer Guide (2026 Edition)
==========================================================================================
Covers:
  - React 19          (JSX, Components, State/Props, Core Hooks, Actions, useActionState, use(), Metadata hoisting)
  - Next.js 16        (App Router, Server/Client components, Fetching, 4 Caching Tiers, 'use cache', Server Actions Security, PPR)
  - Tailwind CSS v4   (Oxide engine, CSS-first config, Container Queries)
  - Best Practices    (Checklists, Anti-patterns)
"""

import paperforge_notes as pn
import paperforge_diagrams as pd

# ---------------------------------------------------------------------------
# CUSTOM DEVELOPER DARK THEME
# ---------------------------------------------------------------------------
dev_dark = pn.DARK.copy_with(
    name="React Next Developer Dark",
    bg="#090d16",  # Premium slate-midnight background
    surface="#121824",  # Dark slate-gray card surface
    surface_alt="#1b2336",  # Border and grid dividers
    card_mid="#121824",
    text="#e4eaf4",  # High-contrast soft white text
    text_dim="#8ca0ba",  # Secondary muted gray-blue text
    text_code="#82b1ff",  # Bright blue for code inline keywords
    accent="#00d8ff",  # Official React brand cyan for borders and titles!
    accent2="#ff4b5c",  # Rose-red secondary accent
    cyan="#00d8ff",
    green="#4caf50",
    green_bg="#0a1d10",
    yellow="#ffb300",
    yellow_bg="#211702",
    red="#ff4b5c",
    red_bg="#220a0d",
    purple="#bc8cff",
    purple_bg="#190e2b",
    white="#f0f6fc",
    border="#1e293b",
    table_hdr="#1e293b",  # Matching slate table header background
    table_bdr="#1e293b",  # Slate table borders
    code_bg="#0f172a",  # Deep slate for code blocks (VS Code styling)
    body_font="Helvetica",
    heading_font="Helvetica-Bold",
    code_font="Courier",
    size_body=10.0,
    size_question=10.0,
)

pn.set_theme(dev_dark)
diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

CW = pn.CW

pn.set_global_header(
    left="React.js & Next.js Industry Guide",
    center="Frontend Reference Booklet",
    right="2026 Edition",
)
pn.set_global_footer(
    left="React 19  -  Next.js 16  -  Tailwind CSS v4",
    show_page_num=True,
)

# ---------------------------------------------------------------------------
# COVER PAGE
# ---------------------------------------------------------------------------
pn.bookmark("Cover Page")
pn.suppress_header(page_only=True)
pn.suppress_footer(page_only=True)
pn.sp(20)
pn.cover_card("React.js & Next.js", "Fundamentals with Tailwind CSS")
pn.cover_subtitle(
    [
        "A COMPLETE DEVELOPER GUIDE  -  INDUSTRY EDITION 2026",
        "React 19  -  Next.js 16 (App Router, Turbopack)  -  Tailwind CSS v4",
    ]
)
pn.sp(20)
pn.image(
    "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=600&h=300&q=80",
    width=320,
    height=160,
    caption="Modern Front-End Web Engineering Stack",
    fallbacks=[
        "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=600&h=300&q=80"
    ],
)
pn.sp(15)
pn.br()

# ---------------------------------------------------------------------------
# TABLE OF CONTENTS
# ---------------------------------------------------------------------------
pn.suppress_header(page_only=True)
pn.suppress_footer(page_only=True)
pn.toc(style="standard")

# ===========================================================================
# PART I -- REACT.JS FUNDAMENTALS
# ===========================================================================
pn.part_box("Part I: React.js Fundamentals (React 19)")

# ---------------------------------------------------------------------------
# 1.1 JSX, Virtual DOM & Component Architecture
# ---------------------------------------------------------------------------
pn.chap_box("1.1 JSX, Virtual DOM & Component Architecture")

pn.section("Project Setup: React 19 with Vite")
pn.body(
    "Vite is the recommended modern build tool for creating standalone React applications. "
    "To scaffold a new React 19 project, follow these shell commands in your terminal:"
)
pn.code_block(
    """# 1. Scaffold a new Vite project (choose React and TypeScript/JavaScript)
npm create vite@latest my-react-app -- --template react-ts

# 2. Navigate into the project directory
cd my-react-app

# 3. Install core dependencies
npm install

# 4. Explicitly upgrade React and React DOM to the latest v19
npm install react@latest react-dom@latest
npm install --save-dev @types/react@latest @types/react-dom@latest

# 5. Launch the local developer server
npm run dev""",
    lang="bash",
)

pn.section("What is JSX?")
pn.body(
    "JSX is a syntax extension for JavaScript that allows you to write HTML-like "
    "markup directly inside JavaScript/TypeScript files. It compiles down to plain "
    "React.createElement(...) calls (or the automatic JSX runtime transform) and is "
    "not parsed directly by browsers. Bundling engines (like Turbopack or SWC/esbuild) "
    "transpile this syntax at build time."
)
pn.code_block(
    """function Greeting({ name }) {
  // JSX compiles to react/jsx-runtime calls
  return <h1 className="text-xl font-semibold">Hello, {name}!</h1>;
}

export default Greeting;""",
    lang="jsx",
)

pn.section("Component Architecture & Props")
pn.definition(
    "A component is a JavaScript function returning JSX that defines a piece of UI. "
    "Props (properties) are read-only configuration arguments passed from a parent component "
    "down to a child, forming a strict one-way data flow."
)
pn.bullet(
    [
        "Component names must start with a capital letter (PascalCase) to distinguish them from native HTML tags.",
        "Props are immutable. A component must never modify its own props; instead, it triggers state changes in the parent.",
        "Use destructuring in the function signature for clean, readable prop access.",
        "The children prop is a special parameter used for nested component composition.",
    ]
)

pn.subsection("Composition Example")
pn.code_block(
    """function Card({ title, children }) {
  return (
    <div className="rounded-lg border p-4 shadow-premium bg-slate-900">
      <h2 className="font-bold text-brand-primary">{title}</h2>
      <div className="mt-2 text-sm">{children}</div>
    </div>
  );
}

function App() {
  return (
    <Card title="User Profile">
      <p>Bharat Dangi - Lead Frontend Engineer</p>
    </Card>
  );
}""",
    lang="jsx",
)

pn.note(
    "<b>Reference:</b> For further details, see the official <a href='https://react.dev'><font color='#00d8ff'>React 19 Documentation</font></a> "
    "and <a href='https://vite.dev'><font color='#00d8ff'>Vite Project Scaffolding Guide</font></a>."
)

# ---------------------------------------------------------------------------
# 1.2 State Management & Core Hooks
# ---------------------------------------------------------------------------
pn.chap_box("1.2 State Management & Core Hooks")

pn.body(
    "Hooks let functional components manage state, refs, context, and side effects. "
    "They must always be called in the same order on every render -- never inside "
    "loops, conditionals, or nested functions."
)
pn.info_table(
    ["Hook Name", "Purpose & Execution Context", "Hook Signature Example"],
    [
        [
            "useState",
            "Manages local component state; updates trigger a component re-render.",
            "const [count, setCount] = useState(0);",
        ],
        [
            "useRef",
            "Holds a mutable value persisting across renders; updates do NOT trigger re-renders.",
            "const timerRef = useRef(null);",
        ],
        [
            "useContext",
            "Reads values from a Context Provider without prop drilling.",
            "const theme = useContext(ThemeContext);",
        ],
        [
            "useMemo",
            "Memoizes an expensive computed calculation between renders.",
            "const memoVal = useMemo(() => calc(a), [a]);",
        ],
        [
            "useCallback",
            "Memoizes a function reference to avoid unnecessary child renders.",
            "const cb = useCallback(() => handler(), []);",
        ],
    ],
    col_widths=["18%", "45%", "37%"],
)
pn.code_block(
    """import { useState, useRef } from "react";

function Timer() {
  const [seconds, setSeconds] = useState(0);
  const intervalRef = useRef(null);

  const startTimer = () => {
    if (intervalRef.current !== null) return;
    intervalRef.current = setInterval(() => {
      setSeconds((s) => s + 1);
    }, 1000);
  };

  const stopTimer = () => {
    clearInterval(intervalRef.current);
    intervalRef.current = null;
  };

  return (
    <div className="flex gap-4">
      <p>Time elapsed: {seconds}s</p>
      <button onClick={startTimer}>Start</button>
      <button onClick={stopTimer}>Stop</button>
    </div>
  );
}""",
    lang="jsx",
)

pn.note(
    "<b>Reference:</b> Read the complete <a href='https://react.dev/reference/react'><font color='#00d8ff'>React Hooks API Reference</font></a>."
)

# ---------------------------------------------------------------------------
# 1.3 Side Effects & Lifecycle Rules
# ---------------------------------------------------------------------------
pn.chap_box("1.3 Side Effects & Lifecycle Rules")

pn.body(
    "Side effects (like API requests, DOM manipulation, or subscriptions) should "
    "be managed using useEffect. The dependency array dictates when the effect re-runs."
)
pn.bullet(
    [
        "<b>No Dependency Array:</b> Runs after <i>every single render</i>. Avoid this, as it causes performance degradation.",
        "<b>Empty Array []:</b> Runs only <i>once</i>, immediately after the component mounts.",
        "<b>With Dependencies [a, b]:</b> Runs on mount, and then re-runs whenever any dependency value changes.",
        "<b>Cleanup Function:</b> Returning a function from useEffect executes it when the component unmounts or before re-running the effect, clearing intervals and event listeners.",
    ]
)
pn.code_block(
    """import { useEffect, useState } from "react";

function WindowResizeListener() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", handleResize);

    // Cleanup function executes on unmount
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []); // Empty array: setup and teardown once on mount/unmount

  return <p>Window Width: {width}px</p>;
}""",
    lang="jsx",
)

pn.note(
    "<b>Reference:</b> For a deep dive into side effects, read the official <a href='https://react.dev/reference/react/useEffect'><font color='#00d8ff'>useEffect API Guide</font></a>."
)

# ---------------------------------------------------------------------------
# 1.4 React 19 Actions & Forms
# ---------------------------------------------------------------------------
pn.chap_box("1.4 React 19 Actions & Forms")

pn.body(
    "React 19 simplifies async operations by integrating Actions directly with forms. "
    "Instead of writing manual state hooks for loading, error, and validation, Actions "
    "manage this automatically via native HTML &lt;form&gt; elements."
)
pn.bullet(
    [
        "<b>Uncontrolled Forms:</b> Input elements use standard 'name' properties. The action receives a native 'FormData' object directly.",
        "<b>useActionState:</b> Takes an action handler and returns `[state, formAction, isPending]`, managing the action's response and state transitions.",
        "<b>useFormStatus:</b> Executed inside nested children of a &lt;form&gt; to read submission details (pending status, form action, input data).",
        "<b>useOptimistic:</b> Shows temporary optimistic UI values during async resolution.",
    ]
)
pn.code_block(
    """// submit-button.jsx
import { useFormStatus } from "react-dom";

export function SubmitButton() {
  const { pending } = useFormStatus(); // Reads status of parent form
  return (
    <button type="submit" disabled={pending} className="bg-brand px-4 py-2">
      {pending ? "Submitting..." : "Save"}
    </button>
  );
}

// user-form.jsx
import { useActionState } from "react";
import { SubmitButton } from "./submit-button";

async function saveProfile(prevState, formData) {
  const username = formData.get("username");
  try {
    await updateProfileAPI(username);
    return { success: true, message: "Profile saved!" };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

export function UserForm() {
  const [state, formAction] = useActionState(saveProfile, null);

  return (
    <form action={formAction} className="space-y-4">
      <input name="username" type="text" className="border p-2" />
      <SubmitButton />
      {state?.error && <p className="text-red-500">{state.error}</p>}
      {state?.success && <p className="text-green-500">{state.message}</p>}
    </form>
  );
}""",
    lang="jsx",
)

pn.note(
    "<b>Reference:</b> For React 19 Actions, check <a href='https://react.dev/reference/react/useActionState'><font color='#00d8ff'>useActionState API</font></a> "
    "and <a href='https://react.dev/reference/react-dom/hooks/useFormStatus'><font color='#00d8ff'>useFormStatus Reference</font></a>."
)

# ---------------------------------------------------------------------------
# 1.5 The use() Hook & Conditional Resources
# ---------------------------------------------------------------------------
pn.chap_box("1.5 The use() Hook & Conditional Resources")

pn.body(
    "The use() hook is a new React 19 API designed to resolve Promises or Context values "
    "conditionally during rendering. Unlike standard hooks, use() can be placed "
    "inside conditionals (if blocks) or loops, integrating natively with React Suspense."
)
pn.code_block(
    """import { use, Suspense } from "react";

function UserProfile({ fetchPromise }) {
  // Suspends execution if fetchPromise is pending
  const userData = use(fetchPromise);
  return <h2>Hello, {userData.name}!</h2>;
}

export default function App() {
  const userPromise = getUserInfo(); // Returns a Promise
  return (
    <Suspense fallback={<div>Resolving User Profile...</div>}>
      <UserProfile fetchPromise={userPromise} />
    </Suspense>
  );
}""",
    lang="jsx",
)

pn.note(
    "<b>Reference:</b> For conditional resource loading, check the <a href='https://react.dev/reference/react/use'><font color='#00d8ff'>use() Hook Documentation</font></a>."
)

# ---------------------------------------------------------------------------
# 1.6 Document Metadata & Asset Hoisting
# ---------------------------------------------------------------------------
pn.chap_box("1.6 Document Metadata & Asset Hoisting")

pn.body(
    "React 19 includes native hoisting support for metadata tags. You can render "
    "&lt;title&gt;, &lt;meta&gt;, and &lt;link&gt; tags anywhere within the component "
    "tree, and React automatically hoists them to the HTML &lt;head&gt; section of the document, "
    "simplifying dynamic SEO configurations."
)
pn.code_block(
    """export function ArticlePage({ article }) {
  return (
    <article className="prose">
      {/* Automatically hoisted to document <head> */}
      <title>{article.title}</title>
      <meta name="description" content={article.excerpt} />
      <link rel="canonical" href={`https://dev.com/blog/${article.slug}`} />

      <h1>{article.title}</h1>
      <p>{article.content}</p>
    </article>
  );
}""",
    lang="jsx",
)

pn.note(
    "<b>Reference:</b> Read more about React 19's native metadata hoisting in the <a href='https://react.dev/reference/react-dom/components/title'><font color='#00d8ff'>Document Metadata Guide</font></a>."
)

# ---------------------------------------------------------------------------
# 1.7 Component Tree & Reconciliation Flow
# ---------------------------------------------------------------------------
pn.chap_box("1.7 Component Tree & Reconciliation Flow")

pn.body(
    "React constructs a virtual component representation. When a state update is triggered, "
    "React calculates the modifications top-down (reconciliation) and commits only the minimal "
    "set of changes to the real browser DOM."
)

fc_tree = pd.Flowchart(
    width=CW,
    height=260,
    caption="Fig 1: Sample Component Tree Layout",
    theme=diag_theme,
)
fc_tree.process("app", "App")
fc_tree.process("header", "Header")
fc_tree.process("main", "MainContent")
fc_tree.process("footer", "Footer")
fc_tree.process("nav", "NavBar")
fc_tree.process("card1", "ProductCard")
fc_tree.process("card2", "ProductCard")
fc_tree.edge("app", "header")
fc_tree.edge("app", "main")
fc_tree.edge("app", "footer")
fc_tree.edge("header", "nav")
fc_tree.edge("main", "card1")
fc_tree.edge("main", "card2")
pn.add(fc_tree.as_flowable())

fc_render = pd.Flowchart(
    width=CW,
    height=300,
    caption="Fig 2: Render & Reconciliation Flow",
    theme=diag_theme,
)
fc_render.terminal("trigger", "State or props change")
fc_render.process("render", "React re-renders affected component(s)")
fc_render.process("vdom", "New virtual DOM tree is built")
fc_render.process("diff", "Diff against previous virtual DOM (reconciliation)")
fc_render.process("commit", "Minimal DOM mutations are committed")
fc_render.terminal("paint", "Browser paints updated UI")
fc_render.edge("trigger", "render")
fc_render.edge("render", "vdom")
fc_render.edge("vdom", "diff")
fc_render.edge("diff", "commit")
fc_render.edge("commit", "paint")
pn.add(fc_render.as_flowable())

pn.rule()
pn.br()

# ===========================================================================
# PART II -- NEXT.JS APP ROUTER
# ===========================================================================
pn.part_box("Part II: Next.js App Router (Next.js 16)")

# ---------------------------------------------------------------------------
# 2.1 File-System Routing
# ---------------------------------------------------------------------------
pn.chap_box("2.1 App Router File-System Routing")

pn.section("Project Setup: Next.js 16 App Router")
pn.body(
    "Next.js provides an automated CLI utility that configures TypeScript, Tailwind CSS, ESLint, "
    "and the app/ directory router out of the box. Run this command to initialize a new project:"
)
pn.code_block(
    """# Scaffold a new Next.js 16 project with modern defaults
npx create-next-app@latest my-next-app \\
  --typescript \\
  --tailwind \\
  --eslint \\
  --app \\
  --src-dir

# Navigate and start dev server with Turbopack enabled by default
cd my-next-app
npm run dev""",
    lang="bash",
)

pn.body(
    "Next.js uses a directory-based router inside the app/ directory. Folders "
    "define URL path segments, while special files define layout and page behavior."
)
pn.info_table(
    ["Special File", "Role & Layout Purpose", "Rendering Context"],
    [
        [
            "page.tsx",
            "Defines the unique page content, mapping a folder route to a URL.",
            "Server Component by default",
        ],
        [
            "layout.tsx",
            "Shared UI wrapping a segment and children; preserves state across page navigation.",
            "Server Component by default",
        ],
        [
            "loading.tsx",
            "Wraps siblings in a Suspense boundary to show automatic loading states.",
            "Server Component",
        ],
        [
            "error.tsx",
            "Defines an Error Boundary UI to catch runtime routing errors.",
            "Client Component ('use client')",
        ],
        [
            "not-found.tsx",
            "Displayed when the notFound() method is called or when no path matches.",
            "Server Component",
        ],
        [
            "route.ts",
            "Exports HTTP methods (GET, POST, etc.) for API endpoint handling.",
            "Server-side Node.js / Edge",
        ],
    ],
    col_widths=["20%", "52%", "28%"],
)

pn.subsection("Dynamic, Catch-All & Route Groups")
pn.bullet(
    [
        "<b>Dynamic Segments [slug]:</b> Maps a dynamic folder path, e.g. app/posts/[slug]/page.tsx matches /posts/hello-world.",
        "<b>Catch-All [...slug]:</b> Maps all nested path segments, e.g. app/docs/[...slug]/page.tsx matches /docs/api/v1/auth.",
        "<b>Optional Catch-All [[...slug]]:</b> Similar to catch-all, but also matches the root parent path (e.g. /docs).",
        "<b>Route Groups (group):</b> Organizes directories visually without affecting the public URL path schema.",
    ]
)

pn.section("How Routes and Pages are Created")
pn.body(
    "To define a route segment in the Next.js App Router, you create a folder inside the "
    "<b>app/</b> directory. To make that route publicly accessible, you place a "
    "<b>page.tsx</b> (or page.jsx) file inside that folder. Nested folders automatically "
    "create nested path segments. For example, <b>app/blog/page.tsx</b> maps to <b>/blog</b>, "
    "while <b>app/blog/details/page.tsx</b> maps to <b>/blog/details</b>."
)
pn.body(
    "Here is an example ASCII folder structure of a typical Next.js project showing App Router "
    "route nesting, special files (like layouts, error states, and proxy handlers), and configuration:"
)
pn.code_block(
    r"""my-next-app/
|-- app/
|   |-- layout.tsx         # Global Root Layout
|   |-- page.tsx           # Homepage (/)
|   |-- proxy.ts           # Node.js Network Proxy
|   |-- blog/
|   |   |-- page.tsx       # Blog list page (/blog)
|   |   `-- [slug]/
|   |       `-- page.tsx   # Dynamic post page (/blog/hello-world)
|   `-- api/
|       `-- users/
|           `-- route.ts   # GET/POST API endpoint
|-- public/
|   `-- vercel.svg
|-- package.json
|-- next.config.ts         # Next.js configuration
|-- tsconfig.json
`-- postcss.config.mjs     # PostCSS Configuration""",
    lang="text",
)

pn.section("Dynamic Routes & Async Parameter Resolution (Next.js 16)")
pn.body(
    "Dynamic segments are defined using square brackets: <b>[segmentName]</b>. In Next.js 16, "
    "synchronous access to <b>params</b> and <b>searchParams</b> is fully removed. Both fields "
    "are now returned as Promises and must be explicitly awaited in Server Components (Page, Layout, "
    "and Route Handlers) or unwrapped using React's <b>use()</b> hook in Client Components."
)
pn.code_block(
    """// app/posts/[slug]/page.tsx (Next.js 16 Asynchronous Params)
interface PageProps {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}

export default async function PostPage({ params, searchParams }: PageProps) {
  // params and searchParams are Promises; we must await them
  const resolvedParams = await params;
  const resolvedSearchParams = await searchParams;
  
  const slug = resolvedParams.slug;
  const sortBy = resolvedSearchParams.sortBy || "date";
  
  return (
    <div className="p-6 bg-slate-900 rounded-lg">
      <h1 className="text-2xl font-bold">Post: {resolvedParams.slug}</h1>
      <p className="text-sm text-dim">Sorting by: {sortBy}</p>
    </div>
  );
}""",
    lang="tsx",
)

pn.note(
    "<b>Reference:</b> Read the official <a href='https://nextjs.org/docs'><font color='#00d8ff'>Next.js Documentation</font></a> "
    "and the <a href='https://nextjs.org/docs/app/getting-started/project-structure'><font color='#00d8ff'>Project Structure & Organization Guide</font></a>."
)

# ---------------------------------------------------------------------------
# 2.2 Server vs Client Components
# ---------------------------------------------------------------------------
pn.chap_box("2.2 Server Components vs Client Components")

pn.definition(
    "Every component inside the App Router is a Server Component by default, rendering "
    "completely on the server, accessing databases directly, and shipping zero JS. "
    "Adding the 'use client' directive at the very top of a file declares it (and its imports) "
    "as a Client Component, enabling browser-only hook execution."
)
pn.info_table(
    ["Capability", "Server Component (Default)", "Client Component ('use client')"],
    [
        ["Access Server Resources (DB, secrets)", "Yes (direct)", "No"],
        ["State and Hooks (useState, useEffect)", "No", "Yes"],
        ["Ships JavaScript to Client Bundle", "No (0 KB)", "Yes (adds to bundle)"],
        ["Render Location", "Server-only", "Server pre-rendered, client hydrated"],
    ],
    col_widths=["30%", "35%", "35%"],
)

pn.subsection("Data Serialization Boundary")
pn.body(
    "When a Server Component passes props down to a Client Component, the data "
    "must cross the server-client network bridge. Therefore, all props passed across "
    "this boundary must be JSON-serializable."
)
pn.bullet(
    [
        "<b>Allowed:</b> Primitives, plain arrays/objects, Map, Set, FormData, and Promises (resolved on the client).",
        "<b>Forbidden:</b> Functions, class instances with methods, React element trees, and browser DOM elements.",
    ]
)

pn.note(
    "<b>Reference:</b> Read more about <a href='https://nextjs.org/docs/app/building-your-application/rendering/server-components'><font color='#00d8ff'>React Server Components (RSC)</font></a> "
    "and Client Components in the Next.js documentation."
)

# ---------------------------------------------------------------------------
# 2.3 Data Fetching & Caching
# ---------------------------------------------------------------------------
pn.chap_box("2.3 Data Fetching & Caching")

pn.body(
    "Next.js extends the web fetch() API to enable granular caching control. "
    "Next.js 16 introduces the stable 'use cache' directive for function-level caching."
)
pn.code_block(
    """// app/services/products.ts
export async function getCachedProduct(productId: string) {
  'use cache'; // Function-level caching! Caches return value automatically.
  return await db.product.findUnique({ where: { id: productId } });
}

// app/products/page.tsx
async function Products() {
  const res = await fetch("https://api.example.com/products", {
    next: { revalidate: 60, tags: ["products"] }, // ISR: refresh cache every 60s
  });
  const products = await res.json();
  
  return (
    <ul>
      {products.map((p) => <li key={p.id}>{p.name}</li>)}
    </ul>
  );
}""",
    lang="tsx",
)

pn.subsection("The Four Caching Tiers")
pn.info_table(
    ["Cache Tier", "Storage Location", "Scope & Invalidation", "Control Override"],
    [
        [
            "Request Memoization",
            "Server Memory",
            "Lasts for the duration of a single page render cycle. Clears automatically.",
            "Wrap calls in React's cache() utility.",
        ],
        [
            "Data Cache",
            "Persistent Disk (Server)",
            "Persists across requests. Invalidate via revalidatePath() or revalidateTag().",
            "fetch(url, { cache: 'no-store' })",
        ],
        [
            "Full Route Cache",
            "Persistent Disk (Server)",
            "HTML and RSC payload generated at build time. Invalidated on revalidation.",
            "Opt-out using cookies(), headers(), or searchParams.",
        ],
        [
            "Router Cache",
            "Client Browser Memory",
            "Stores page layouts in browser during a session. Cleared on refresh.",
            "Set &lt;Link prefetch={false}&gt; or call router.refresh().",
        ],
    ],
    col_widths=["20%", "20%", "30%", "30%"],
)

pn.note(
    "<b>Reference:</b> Read more about data fetching and caching directives in the <a href='https://nextjs.org/docs/app/building-your-application/data-fetching'><font color='#00d8ff'>Next.js Data Fetching Guide</font></a>."
)

# ---------------------------------------------------------------------------
# 2.4 Server Actions & Security
# ---------------------------------------------------------------------------
pn.chap_box("2.4 Server Actions & Security")

pn.body(
    "Server Actions are async functions compiled as secure POST endpoints. "
    "Because they are publicly accessible, actions must implement strict validation checks."
)
pn.bullet(
    [
        "<b>Zod Input Validation:</b> Never trust incoming arguments directly. Always validate payloads using schemas.",
        "<b>Authentication Checks:</b> Verify caller identity using session credentials (cookies(), headers()) inside the action body.",
        "<b>Rate Limiting:</b> Restrict execution frequencies on sensitive API triggers to prevent abuse and DDoS attacks.",
    ]
)
pn.code_block(
    """// app/actions/comment.ts
'use server';

import { z } from "zod";
import { auth } from "@/lib/auth";
import { rateLimit } from "@/lib/rate-limit";
import { revalidatePath } from "next/cache";

const schema = z.object({
  postId: z.string().uuid(),
  text: z.string().min(1).max(250),
});

export async function addComment(rawInput: unknown) {
  const user = await auth();
  if (!user) throw new Error("Unauthorized");

  // Prevent spamming
  await rateLimit(user.id, "add-comment", 5);

  const input = schema.parse(rawInput); // Enforce schema
  await db.comment.create({
    data: { postId: input.postId, content: input.text, authorId: user.id }
  });

  revalidatePath(`/posts/${input.postId}`);
}""",
    lang="tsx",
)

pn.note(
    "<b>Reference:</b> Read more about action security in the <a href='https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations'><font color='#00d8ff'>Next.js Server Actions Guide</font></a>."
)

# ---------------------------------------------------------------------------
# 2.5 Rendering Strategies & Streaming
# ---------------------------------------------------------------------------
pn.chap_box("2.5 Rendering Strategies & Streaming")

pn.body(
    "Next.js supports multiple rendering models: Static (SSG), Incremental Static "
    "Regeneration (ISR), Dynamic (SSR), and Client-Side Rendering (CSR). "
    "Partial Prerendering (PPR) acts as a hybrid by merging static layout shells with "
    "streamed dynamic content."
)

seq = pd.SequenceDiagram(
    width=CW,
    height=300,
    caption="Fig 3: Streaming Request Lifecycle",
    theme=diag_theme,
    margin=60.0,
)
seq.actor("browser", "Browser")
seq.actor("server", "Next.js Server")
seq.actor("data", "Database / API")
seq.message("browser", "server", "GET /dashboard", arrow="solid")
seq.activate("server")
seq.message("server", "browser", "Stream: static HTML layout shell", arrow="dashed")
seq.message("server", "data", "Fetch dynamic database metrics", arrow="solid")
seq.activate("data")
seq.message("data", "server", "Data resolved", arrow="dashed")
seq.deactivate("data")
seq.message(
    "server", "browser", "Stream: resolved Suspense component payload", arrow="dashed"
)
seq.deactivate("server")
seq.message(
    "browser", "browser", "Hydrate client interaction hooks", arrow="solid_open"
)
pn.add(seq.as_flowable())

pn.note(
    "<b>Reference:</b> Read more about Partial Prerendering and streaming in the <a href='https://nextjs.org/docs/app/building-your-application/rendering/partial-prerendering'><font color='#00d8ff'>Next.js PPR Guide</font></a>."
)

# ---------------------------------------------------------------------------
# 2.6 Middleware & Route Handlers
# ---------------------------------------------------------------------------
pn.chap_box("2.6 Middleware & Route Handlers")

pn.section("Middleware & Network Proxy (proxy.ts)")
pn.body(
    "Next.js 16 introduces <b>proxy.ts</b> as the network proxy layer running on the "
    "Node.js runtime, permitting full database access and standard Node.js APIs. "
    "The entry function is exported as <b>proxy</b>. If Edge-only features are needed "
    "(like geolocation and low-latency rewrites), <b>middleware.ts</b> can still be used."
)
pn.code_block(
    """// proxy.ts (Next.js 16 Node.js network proxy)
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  const sessionToken = request.cookies.get("session-token")?.value;
  
  // Auth guard: redirect to login if no session is active
  if (request.nextUrl.pathname.startsWith("/dashboard") && !sessionToken) {
    return NextResponse.redirect(new URL("/login", request.url));
  }
  
  const response = NextResponse.next();
  response.headers.set("X-Frame-Options", "DENY");
  return response;
}

export const config = {
  matcher: ["/dashboard/:path*"],
};""",
    lang="tsx",
)

pn.section("Route Handlers")
pn.body(
    "Route Handlers (route.ts) execute custom request handlers on the server side, "
    "replacing the legacy pages/api structure."
)
pn.code_block(
    """// app/api/users/route.ts
import { NextResponse } from "next/server";

export async function GET() {
  const users = await db.user.findMany();
  return NextResponse.json(users);
}

export async function POST(request: Request) {
  const payload = await request.json();
  const newUser = await db.user.create({ data: payload });
  return NextResponse.json(newUser, { status: 201 });
}""",
    lang="tsx",
)

pn.note(
    "<b>Reference:</b> Read more about proxy routing in <a href='https://nextjs.org/docs/app/api-reference/file-conventions/proxy'><font color='#00d8ff'>Next.js Proxy API Reference</font></a> "
    "and custom APIs in the <a href='https://nextjs.org/docs/app/building-your-application/routing/route-handlers'><font color='#00d8ff'>Route Handlers Guide</font></a>."
)
pn.br()

# ===========================================================================
# PART III -- TAILWIND CSS V4
# ===========================================================================
pn.part_box("Part III: Tailwind CSS v4 Basics")

# ---------------------------------------------------------------------------
# 3.1 Utility-First & CSS-First Setup
# ---------------------------------------------------------------------------
pn.chap_box("3.1 Utility-First & CSS-First Setup")

pn.section("Project Setup: Tailwind CSS v4 Integration")
pn.body(
    "If you are adding Tailwind CSS v4 manually to a custom or existing bundler project (such as Next.js "
    "without auto-config), follow these installation and config steps:"
)
pn.code_block(
    """# 1. Install Tailwind CSS v4 and its corresponding PostCSS wrapper
npm install tailwindcss @tailwindcss/postcss postcss

# 2. Add the plugin to your postcss.config.mjs configuration file
// postcss.config.mjs
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
};

# 3. Import Tailwind directives at the top of your global CSS stylesheet
// app/globals.css
@import "tailwindcss";""",
    lang="bash",
)

pn.body(
    "Tailwind CSS v4 introduces a completely rewritten Rust compilation engine (Oxide) "
    "designed to increase build performance up to 10x. Config has shifted from "
    "javascript configurations (tailwind.config.js) to CSS-first styling configs using standard "
    "@theme directives."
)
pn.code_block(
    """/* app/globals.css */
@import "tailwindcss";

@theme {
  --color-brand-primary: #00d8ff; /* React brand cyan */
  --color-brand-dark: #090d16;
  
  --font-sans: "Outfit", sans-serif;
  --font-mono: "Fira Code", monospace;
  
  --shadow-premium: 0 4px 25px -4px rgba(0, 0, 0, 0.25);
}""",
    lang="css",
)
pn.note(
    "Tailwind v4 features automatic content scanning out of the box, meaning you "
    "no longer need to configure path lists manually."
)

# ---------------------------------------------------------------------------
# 3.2 Spacing, Sizing & Typography
# ---------------------------------------------------------------------------
pn.chap_box("3.2 Spacing, Sizing & Typography")

pn.body(
    "Tailwind layout designs are composed using granular utilities. This cheat sheet "
    "summarizes the core utility categories used daily in frontend mockups."
)
pn.info_table(
    ["Category", "CSS Properties Mapped", "Utility Classes Examples"],
    [
        [
            "Flexbox",
            "display: flex, flex-direction, align-items, justify-content",
            "flex, flex-row, items-center, justify-between, gap-4",
        ],
        [
            "CSS Grid",
            "display: grid, grid-template-columns, gap spacing",
            "grid, grid-cols-4, gap-6, col-span-2",
        ],
        [
            "Sizing",
            "width, height, max-width, min-height",
            "w-full, w-64, h-screen, max-w-xl, min-h-0",
        ],
        ["Spacing", "padding, margin", "p-4, px-6, py-2, m-auto, mt-4, -space-x-2"],
        [
            "Typography",
            "font-family, font-size, font-weight, line-height",
            "font-sans, text-lg, font-bold, leading-tight, tracking-wide",
        ],
        [
            "Effects",
            "box-shadow, opacity, backdrop-filter blur",
            "shadow-premium, opacity-80, backdrop-blur-md",
        ],
    ],
    col_widths=["22%", "43%", "35%"],
)

pn.note(
    "<b>Reference:</b> For styling setup, check the <a href='https://tailwindcss.com/docs'><font color='#00d8ff'>Tailwind CSS v4 Documentation</font></a> "
    "and <a href='https://tailwindcss.com/docs/utility-first-fundamentals'><font color='#00d8ff'>Utility-First Fundamentals</font></a>."
)

# ---------------------------------------------------------------------------
# 3.3 Responsive & State Variants
# ---------------------------------------------------------------------------
pn.chap_box("3.3 Responsive & State Variants")

pn.body(
    "Tailwind prefixes utilities with variants to apply them conditionally—for "
    "different screen widths (mobile-first design) or pseudo-states like hover and active."
)
pn.bullet(
    [
        "<b>Responsive Breakpoints:</b> Mobile-first schema: sm (640px), md (768px), lg (1024px), xl (1280px), 2xl (1536px). md:px-6 applies only on md screens and wider.",
        "<b>User States:</b> hover, focus, active, disabled, focus-visible.",
        "<b>Advanced Variants:</b> group-hover and peer-focus allow styling children or adjacent siblings based on active parent or peer interactions.",
    ]
)
pn.code_block(
    """<div className="group border p-4 hover:border-brand-primary">
  <h3 className="text-gray-400 group-hover:text-white">
    Hovering parent changes title color!
  </h3>
  <input type="text" className="peer border p-2" />
  <p className="hidden peer-focus:block text-xs">
    Showing help text when input is focused!
  </p>
</div>""",
    lang="jsx",
)

# ---------------------------------------------------------------------------
# 3.4 Container Queries & Named Containers
# ---------------------------------------------------------------------------
pn.chap_box("3.4 Container Queries & Named Containers")

pn.body(
    "Tailwind v4 introduces built-in container queries via `@container` and `@min-*` / `@max-*` variants. "
    "Instead of styling elements based on the overall browser window size, you style elements "
    "based on the parent wrapper's width, enabling modular components."
)
pn.code_block(
    """// Parent container sets container context
<div className="@container border p-4">
  {/* Elements layout shifts based on parent width, not screen width */}
  <div className="grid grid-cols-1 @sm:grid-cols-2 @lg:grid-cols-3 gap-4">
    <div className="p-4 bg-slate-900">Card 1</div>
    <div className="p-4 bg-slate-900">Card 2</div>
    <div className="p-4 bg-slate-900">Card 3</div>
  </div>
</div>

// Named container targeting (Parent names container context)
<div className="@container/sidebar w-64 border-r">
  <div className="@container/main flex-1">
    {/* Style child based specifically on sidebar width */}
    <div className="@lg/sidebar:hidden">Compact Mode</div>
  </div>
</div>""",
    lang="jsx",
)

pn.note(
    "<b>Reference:</b> For state styling and queries, see <a href='https://tailwindcss.com/docs/hover-focus-and-other-states'><font color='#00d8ff'>Breakpoints & State Hover Variants</font></a> "
    "and <a href='https://tailwindcss.com/docs/container-queries'><font color='#00d8ff'>Named Container Queries</font></a>."
)
pn.br()

# ===========================================================================
# PART IV -- BEST PRACTICES & ANTI-PATTERNS
# ===========================================================================
pn.part_box("Part IV: Production Best Practices & Anti-Patterns")

# ---------------------------------------------------------------------------
# 4.1 Production Checklist
# ---------------------------------------------------------------------------
pn.chap_box("4.1 Production Checklist")

pn.body(
    "To deploy highly optimized React/Next.js/Tailwind applications, teams must "
    "enforce strict bundle size, layout shift (CLS), and SEO audits before staging."
)
pn.info_table(
    [
        "Verification Layer",
        "Audit Objective & Best Practice Check",
        "Tooling / Verification",
    ],
    [
        [
            "Bundle Size Optimization",
            "Ensure client bundles ship minimal code. Lazy load heavy widgets using dynamic() imports.",
            "Next.js Bundle Analyzer",
        ],
        [
            "Search Engine Optimization (SEO)",
            "Set correct metadata fields. Use React 19 title and meta elements in dynamic pages.",
            "Lighthouse / Google Search Console",
        ],
        [
            "Layout Performance",
            "Pre-size image dimensions and allocate Suspense shell placeholders to prevent Layout Shift.",
            "Chrome DevTools Core Web Vitals",
        ],
        [
            "ReportLab XML Escaping",
            "Any html tags printed in paragraph body text strings (like &lt;div&gt;) must be escaped to avoid crashes.",
            "python script compilation check",
        ],
    ],
    col_widths=["24%", "48%", "28%"],
)

# ---------------------------------------------------------------------------
# 4.2 Common Front-End Anti-Patterns
# ---------------------------------------------------------------------------
pn.chap_box("4.2 Common Front-End Anti-Patterns")

pn.body(
    "Avoiding common software design pitfalls prevents rendering bugs and "
    "maintains pipeline code health."
)
pn.bullet(
    [
        "<b>Prop Drilling:</b> Passing state down through 5 layers of unused parent components. Solution: Use useContext or state libraries.",
        "<b>useEffect Loop:</b> Triggering a state update inside useEffect without a dependency array, causing infinite render cycles.",
        "<b>Blocking Fetching:</b> Initiating multiple sequential client-side awaits (waterfalls) instead of parallel Promise.all() fetches.",
        "<b>Ignoring Flaky Tests:</b> Letting broken test cases pass without quarantine, which erodes developers' confidence in the CI verification pipeline.",
    ]
)

pn.note(
    "<b>Reference:</b> For production preparation guidelines, see <a href='https://nextjs.org/docs/app/building-your-application/deploying'><font color='#00d8ff'>Next.js Deployment Checklist</font></a>."
)

# ===========================================================================
# QUICK REVISION
# ===========================================================================
pn.chap_box("Quick Revision: React vs Next.js vs Tailwind")

pn.info_table(
    ["Framework / Library", "Primary Problem Solved", "Core Architecture Idea"],
    [
        [
            "React.js",
            "Handles stateful UI updates and layout composition.",
            "Virtual DOM reconciliation, declarative hooks, state flow.",
        ],
        [
            "Next.js",
            "Manages routing, server-side rendering, and data caching.",
            "App Router filesystem, Server/Client boundary, caching tiers.",
        ],
        [
            "Tailwind CSS",
            "Enables rapid, consistent styling without leaving markup.",
            "Utility classes compilation, CSS-first config, Rust Oxide compiler.",
        ],
    ],
    col_widths=["25%", "40%", "35%"],
)

# ---------------------------------------------------------------------------
# BUILD DOCUMENT
# ---------------------------------------------------------------------------
pn.build_doc("react_nextjs_tailwind_notes.pdf")
