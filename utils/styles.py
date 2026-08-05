from pathlib import Path

import setup


def load_stylesheet(filename: str) -> str:
    path = Path(__file__).parent.parent / "styles" / filename

    stylesheet = path.read_text(encoding="utf-8")

    return stylesheet.format(
        LIGHT_COLOR=setup.LIGHT_COLOR,
        MOSS_GREEN=setup.MOSS_GREEN,
        MIDNIGHT_GREEN=setup.MIDNIGHT_GREEN,
        POSE_BROWN=setup.POSE_BROWN,
        DARK_GREEN=setup.DARK_GREEN,
        HOVER_MOSS_GREEN=setup.HOVER_MOSS_GREEN,
        HOVER_POSE_BROWN=setup.HOVER_POSE_BROWN,
        BUFF=setup.BUFF,
    )
