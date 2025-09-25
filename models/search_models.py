"""General search models combining multiple provider search results."""
from typing import Literal, Optional

from pydantic import BaseModel, Field

from .kap_models import EndeksKoduAramaSonucu, SirketAramaSonucu
from .tefas_models import FonAramaSonucu


class GenelAramaSonucu(BaseModel):
    """Aggregated search result combining company, index, and fund matches."""

    arama_terimi: str = Field(description="The original search query that was used.")
    arama_kategorisi: Literal["auto", "company", "index", "fund"] = Field(
        description="Specifies which data domain was searched. 'auto' searches all domains."
    )
    fon_kategorisi: Optional[str] = Field(
        None,
        description="Fund category filter forwarded to TEFAS search when provided.",
    )
    sirket_sonuclari: Optional[SirketAramaSonucu] = Field(
        None,
        description="Matching BIST company results when company search is requested.",
    )
    endeks_sonuclari: Optional[EndeksKoduAramaSonucu] = Field(
        None, description="Matching BIST index results when index search is requested."
    )
    fon_sonuclari: Optional[FonAramaSonucu] = Field(
        None, description="Matching TEFAS fund results when fund search is requested."
    )
    ozet: Optional[str] = Field(
        None,
        description=(
            "Human readable summary describing how many results were returned for each domain."
        ),
    )

