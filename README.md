# David Nehemia

**Building systems that hold up in production and reading the receipts afterwards.**

Based in Indonesia · Full-stack & applied ML

---

I build web applications and machine-learning systems, and I care about the part most portfolios skip: *why* the design decisions were made and what broke along the way. Recent work spans real-time queue systems with hardened database security, deep metric learning for signature verification, and zero-build tooling that runs entirely in a browser.

## Currently building

| Project | What it is | Stack | Status |
| --- | --- | --- | --- |
| [**AstraQueue**](https://astra-queue.vercel.app) | Real-time school queue & leave-permission system. Public display board, admin console, violation ledger (no app server; all authorization enforced by Postgres row-level security). | React 18 · Vite · Tailwind · Supabase | Live · private repo |
| [**ChordApp**](https://chord-app-sand.vercel.app) | Chord transposer for Indonesian worship music. Charts are written once in scale-degree notation and rendered live in any of 12 keys. Single HTML file, no build step. | Vanilla JS · JSON | Live · [source](https://github.com/VidVellichor/ChordApp) |
| **Blizy** | Campus room booking app: availability calendar, booking flow, conflict validation. Frontend production-ready, data layer backend-ready. | React 18 · TypeScript · Vite · Tailwind | Private · demo on request |
| **Signature Verification AI** | Offline signature verification via deep metric learning using EfficientNet-B0 embeddings scored by cosine similarity. Ships with a FastAPI inference backend, a web UI, and an IEEE-style write-up. | PyTorch · FastAPI · Jupyter | Research + demo |
| **Nebula** | AI study companion: turn documents, audio, and video into summaries, flashcards, and an interactive tutor. | React · Vite · Tailwind | In design |

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
