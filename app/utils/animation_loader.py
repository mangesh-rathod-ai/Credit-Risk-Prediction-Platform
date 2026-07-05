import json
from pathlib import Path
from streamlit_lottie import st_lottie
import streamlit as st


def load_animation(category, filename):
    """
    Load a Lottie animation from assets/animations.

    Example:
    load_animation("analytics", "counter.json")
    """

    animation_path = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "animations"
        / category
        / filename
    )

    try:
        with open(animation_path, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        st.warning(f"Animation file not found:\n{animation_path}")
        return None

    except json.JSONDecodeError:
        st.error(f"Invalid JSON file:\n{animation_path}")
        return None


def show_animation(category, filename,
                   height=250,
                   width=None,
                   key=None,
                   speed=1,
                   loop=True):

    animation = load_animation(category, filename)

    if animation:
        st_lottie(
            animation,
            height=height,
            width=width,
            speed=speed,
            loop=loop,
            key=key
        )