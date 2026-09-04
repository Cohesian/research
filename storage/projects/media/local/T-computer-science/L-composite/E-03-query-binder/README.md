# Query Binder scene

This is the accepted standalone export of the Studio scene identified by
`T-computer-science/L-composite/F-03-query-binder`.

It pins Loci and Cohesian's visual plugin, and carries the small local
voiceover adapter used by the scene. It does not import from Studio's mutable
production workspace.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
loci render scenes/scene.py QueryBinder -vq l -vf 30 -ss gtts
```

That command is the inexpensive review path. Reproducing the accepted master
uses `-vq h -vf 30 -ss openai -so voice=alloy,model=tts-1-hd` and requires an
`OPENAI_API_KEY` in the local environment.

[`scene.toml`](scene.toml) records the canonical node identity, entrypoint,
scene class, dependency closure, and accepted master checksum.
