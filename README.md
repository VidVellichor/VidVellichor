# David Nehemia Sunoto

**Building systems that hold up in production and reading the receipts afterwards.**

Based in Indonesia · Full-stack & applied ML

---

I build web applications and machine-learning systems, and I care about the part most portfolios skip: *why* the design decisions were made and what broke along the way. Recent work spans real-time queue systems with hardened database security, deep metric learning for signature verification, and zero-build tooling that runs entirely in a browser.

## What I work with

```
Languages    Python · JavaScript · SQL · HTML/CSS
Frontend     React 18 · Vite · Tailwind CSS · Bootstrap 5
Backend      FastAPI · Express · Node.js
Data / ML    PyTorch · scikit-learn · pandas · Jupyter · deep metric learning
Infra        Supabase (Postgres + RLS) · Vercel · Render · Git
```

## Things I've learned the hard way

- **Security belongs in the database.** AstraQueue's RLS migration exists because permissive `USING (true)` policies are the kind of thing you only notice after someone else finds them.
- **A model that can't be explained isn't finished.** The signature project only became credible once the embedding space could be visualised and the failure cases named.
- **Delete the server you don't need.** ChordApp shipped with an Express + MySQL backend that the deployed site never called. The static JSON version is faster, cheaper, and has less that can break.

## Beyond the terminal

Competitive in Valorant, which is a reasonable amount of patience practice for debugging. I also edit video and shoot content. The same instinct applies: cut anything that doesn't earn its place.

---

*Open to collaboration on applied ML and full-stack work. The fastest way to reach me is to open an issue on one of my repos.*
