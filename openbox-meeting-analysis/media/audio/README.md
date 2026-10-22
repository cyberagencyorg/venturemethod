# Audio storage in GitHub

The lossless transcription derivative is 175,647,576 bytes, exceeding GitHub's ordinary 100 MB per-file limit. In the GitHub upload it is stored losslessly as:

- `meeting-audio-16k-mono.flac.part-aa`
- `meeting-audio-16k-mono.flac.part-ab`

Reconstruct it from this directory with:

```bash
cat meeting-audio-16k-mono.flac.part-* > meeting-audio-16k-mono.flac
sha256sum meeting-audio-16k-mono.flac
```

Expected SHA-256:

```text
d549dc40f51e00610465436d6f624fb0abbb27d35bd46fda17e4283604e7c0e8
```

The split is byte-for-byte reversible; audio was not re-encoded.
