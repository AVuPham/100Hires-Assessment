from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


VIDEO_ID = "4GBlHObjOrY"
OUTPUT_PATH = Path("research/youtube-transcripts/matt-diggity-vid1.md")


def main() -> None:
    # Prefer manually created English subtitles, then auto-generated English.
    transcript = YouTubeTranscriptApi.get_transcript(
        VIDEO_ID,
        languages=["en", "en-US", "en-GB"],
    )

    formatter = TextFormatter()
    plain_text = formatter.format_transcript(transcript).strip()

    markdown = (
        "# Transcript: Matt Diggity Video 1\n\n"
        f"Video: https://www.youtube.com/watch?v={VIDEO_ID}\n\n"
        "## Transcript\n\n"
        f"{plain_text}\n"
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(markdown, encoding="utf-8")
    print(f"Saved transcript to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
