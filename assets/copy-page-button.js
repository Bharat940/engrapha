/**
 * Copy-page button for Mkdocs Material.
 * Appends the Copy button directly to the page <h1> without wrapping.
 * Copies the entire main page content (text) to the clipboard.
 */
(function () {
  var ICON = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"/><path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z"/></svg>';

  var DEFAULT_TEXT = ICON + " Copy page";
  var LOADING_TEXT = '<span style="font-size:11px">Copying…</span>';
  var SUCCESS_TEXT = " Copied!";
  var FAIL_TEXT = " Failed";
  
  var isCopying = false; // Lock to prevent spamming

  function createButton() {
    var heading = document.querySelector(".md-content__inner > .md-typeset > h1:first-of-type")
                  || document.querySelector(".md-typeset h1")
                  || document.querySelector("h1");
    if (!heading) return;

    // Check if button already exists in the heading
    if (heading.querySelector(".copy-page-btn")) return;

    // Use <button type="button"> instead of <a> to avoid "#" anchor getElementById console warnings
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "copy-page-btn";
    btn.title = "Copy page content";
    btn.setAttribute("aria-label", "Copy page content");
    btn.innerHTML = DEFAULT_TEXT;

    btn.addEventListener("click", function (e) {
      e.preventDefault();
      if (isCopying) return; // Prevent spamming
      isCopying = true;
      btn.classList.add("copy-page-btn--disabled");
      copyPageContent(btn);
    });

    // Add CSS class to heading for relative layout
    heading.classList.add("has-copy-page-btn");
    
    // Detect if heading or its parent is center-aligned
    var style = window.getComputedStyle(heading);
    var parentStyle = window.getComputedStyle(heading.parentElement);
    if (
      style.textAlign === "center" ||
      parentStyle.textAlign === "center" ||
      heading.parentElement.getAttribute("align") === "center"
    ) {
      heading.classList.add("copy-page-btn-centered");
    }

    heading.appendChild(btn);
  }

  function copyPageContent(btn) {
    // Select the main page content element
    var contentEl = document.querySelector(".md-content__inner");
    if (!contentEl) {
      showFeedback(btn, false);
      return;
    }

    // Clone the node to avoid mutating the live DOM
    var clone = contentEl.cloneNode(true);
    
    // Strip the copy button itself and any header anchor symbols (e.g. Paragraph links)
    var copyBtns = clone.querySelectorAll(".copy-page-btn");
    copyBtns.forEach(function (cb) {
      cb.remove();
    });
    
    var headerLinks = clone.querySelectorAll("a.headerlink");
    headerLinks.forEach(function (hl) {
      hl.remove();
    });

    var pageText = clone.innerText.trim();

    btn.innerHTML = LOADING_TEXT;

    navigator.clipboard.writeText(pageText).then(function () {
      showFeedback(btn, true);
    }).catch(function () {
      showFeedback(btn, false);
    });
  }

  function showFeedback(btn, success) {
    btn.innerHTML = success ? SUCCESS_TEXT : FAIL_TEXT;
    var color = success
      ? "var(--md-success-fg-color, #3fb950)"
      : "var(--md-error-fg-color, #f85149)";
    btn.style.color = color;
    btn.style.fontWeight = "600";

    setTimeout(function () {
      btn.innerHTML = DEFAULT_TEXT;
      btn.style.color = "";
      btn.style.fontWeight = "";
      btn.classList.remove("copy-page-btn--disabled");
      isCopying = false; // Reset lock
    }, 2000);
  }

  function boot() {
    createButton();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      isCopying = false;
      boot();
    });
  } else {
    document.addEventListener("DOMContentLoaded", boot);
  }
})();
