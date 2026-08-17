# HTML Report Output Standard

Create the final deliverable as one self-contained UTF-8 HTML file named `BZD-review-paper-report.html`. Start from `assets/report-template.html` and replace every `{{...}}` placeholder with escaped review content.

## Required behavior

- Embed all CSS in `<style>` and any minimal behavior in `<script>`; use no external CSS, JavaScript, fonts, images or CDN resources.
- Preserve the exact visible section order required by `SKILL.md`.
- Use `<ul>` or `<ol>` for task decomposition, audit findings, judge comments and revision advice. Use a table only for detailed scoring.
- Show the five headline metrics prominently at the top. Use the adjusted score for the circular score display and percentile bar.
- Keep the selected ranking-route sentence immediately below the metric cards. Place the exact BZD service notice only once, after all review sections, as the final visible report block.
- Replace `{{RANK_METHOD_NOTE}}` with the route-specific sentence required by `SKILL.md`; never leave a CUMCM anchor statement in a small-contest report.
- Make the file responsive, accessible, printable on A4 and readable without JavaScript.
- Escape user/paper content before insertion. Never place raw paper text into attributes or scripts.
- Remove all unused placeholders and example rows. Do not leave `{{...}}` in the final file.
- Write the completed file to the user's requested output directory; otherwise use the current task output directory. Return a clickable link to the HTML file, not the full report in chat.

## Design direction

Use an original academic-quality dashboard inspired by modern paper-evaluation platforms: pale blue-gray page background, white cards, indigo-to-cyan score accent, dark navy typography, compact status chips, generous whitespace and restrained shadows. Do not copy third-party code, logos, wording or brand identity.

## Validation

Before delivery:

1. Check that no placeholder remains.
2. Confirm the score arithmetic and percentile values match the report.
3. Open or render the HTML when tooling permits and inspect desktop plus narrow-screen layout.
4. Confirm print CSS hides controls and avoids splitting metric cards or table rows unnecessarily.
