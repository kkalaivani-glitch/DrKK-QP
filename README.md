# DR. K. KALAIVANI — QP Site

Standalone website for Question Papers (QP) with CO & Bloom’s Taxonomy mapping.

## Pages
- `index.html`: Landing with links to papers
- `qp.html`: CO–BT mapped formal paper
- `sample-paper.html`: Example paper with BT charts

## Local Preview
Use Python HTTP server or any static server.

```powershell
cd "C:\Users\Public\qp-site"; python -m http.server 8001
```
Then open: http://localhost:8001/

## Deploy (GitHub Pages)
- Initialize a new repo and push to GitHub
- In repo Settings → Pages: Source `main` and `/ (root)`
- Visit: `https://<your-username>.github.io/<repo>/`