// Copy button for BibTeX citation boxes. Progressive enhancement: the button
// is rendered with `hidden` and only shown when this script runs, so pages
// without JavaScript simply show selectable BibTeX text.
(function () {
  "use strict";

  function selectText(el) {
    var range = document.createRange();
    range.selectNodeContents(el);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
  }

  function legacyCopy(el) {
    selectText(el);
    try {
      return document.execCommand("copy");
    } catch (e) {
      return false;
    }
  }

  function announce(box, button, message, ok) {
    var status = box.querySelector(".citation__status");
    if (status) status.textContent = message;
    button.textContent = ok ? "Copied" : "Copy";
    window.clearTimeout(button._resetTimer);
    button._resetTimer = window.setTimeout(function () {
      button.textContent = "Copy";
      if (status) status.textContent = "";
    }, 4000);
  }

  document.querySelectorAll(".citation__copy").forEach(function (button) {
    var target = document.getElementById(button.getAttribute("data-copy-target"));
    var box = button.closest(".citation");
    if (!target || !box) return;
    button.hidden = false;

    button.addEventListener("click", function () {
      var text = target.textContent;
      var fail = function () {
        if (legacyCopy(target)) {
          announce(box, button, "BibTeX copied to clipboard.", true);
        } else {
          selectText(target);
          target.focus();
          announce(box, button, "Copying is not available here. The citation is selected: press Ctrl+C (or ⌘C) to copy it.", false);
        }
      };
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(function () {
          announce(box, button, "BibTeX copied to clipboard.", true);
        }, fail);
      } else {
        fail();
      }
    });
  });
})();
