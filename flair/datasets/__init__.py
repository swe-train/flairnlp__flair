# Expose base classses
from .base import (
    DataLoader,
    FlairDatapointDataset,
    MongoDataset,
    SentenceDataset,
    StringDataset,
)

# Expose all biomedical data sets used for the evaluation of BioBERT
# -
# -
# -
# -
# Expose all biomedical data sets using the HUNER splits
# Expose all biomedical data sets
from .biomedical import (
    ANAT_EM,
    AZDZ,
    BC2GM,
    BIO_INFER,
    BIOBERT_CHEMICAL_BC4CHEMD,
    BIOBERT_CHEMICAL_BC5CDR,
    BIOBERT_DISEASE_BC5CDR,
    BIOBERT_DISEASE_NCBI,
    BIOBERT_GENE_BC2GM,
    BIOBERT_GENE_JNLPBA,
    BIOBERT_SPECIES_LINNAEUS,
    BIOBERT_SPECIES_S800,
    BIONLP2013_CG,
    BIONLP2013_PC,
    BIOSEMANTICS,
    CDR,
    CELL_FINDER,
    CEMP,
    CHEMDNER,
    CLL,
    CRAFT,
    CRAFT_V4,
    DECA,
    FSU,
    GELLUS,
    GPRO,
    HUNER_CELL_LINE,
    HUNER_CELL_LINE_CELL_FINDER,
    HUNER_CELL_LINE_CLL,
    HUNER_CELL_LINE_GELLUS,
    HUNER_CELL_LINE_JNLPBA,
    HUNER_CHEMICAL,
    HUNER_CHEMICAL_CDR,
    HUNER_CHEMICAL_CEMP,
    HUNER_CHEMICAL_CHEBI,
    HUNER_CHEMICAL_CHEMDNER,
    HUNER_CHEMICAL_CRAFT_V4,
    HUNER_CHEMICAL_SCAI,
    HUNER_DISEASE,
    HUNER_DISEASE_CDR,
    HUNER_DISEASE_MIRNA,
    HUNER_DISEASE_NCBI,
    HUNER_DISEASE_PDR,
    HUNER_DISEASE_SCAI,
    HUNER_DISEASE_VARIOME,
    HUNER_GENE,
    HUNER_GENE_BC2GM,
    HUNER_GENE_BIO_INFER,
    HUNER_GENE_CELL_FINDER,
    HUNER_GENE_CHEBI,
    HUNER_GENE_CRAFT_V4,
    HUNER_GENE_DECA,
    HUNER_GENE_FSU,
    HUNER_GENE_GPRO,
    HUNER_GENE_IEPA,
    HUNER_GENE_JNLPBA,
    HUNER_GENE_LOCTEXT,
    HUNER_GENE_MIRNA,
    HUNER_GENE_OSIRIS,
    HUNER_GENE_VARIOME,
    HUNER_SPECIES,
    HUNER_SPECIES_CELL_FINDER,
    HUNER_SPECIES_CHEBI,
    HUNER_SPECIES_CRAFT_V4,
    HUNER_SPECIES_LINNEAUS,
    HUNER_SPECIES_LOCTEXT,
    HUNER_SPECIES_MIRNA,
    HUNER_SPECIES_S800,
    HUNER_SPECIES_VARIOME,
    IEPA,
    JNLPBA,
    LINNEAUS,
    LOCTEXT,
    MIRNA,
    NCBI_DISEASE,
    OSIRIS,
    PDR,
    S800,
    SCAI_CHEMICALS,
    SCAI_DISEASE,
    VARIOME,
)

# Expose all document classification datasets
from .document_classification import (
    AGNEWS,
    AMAZON_REVIEWS,
    COMMUNICATIVE_FUNCTIONS,
    GERMEVAL_2018_OFFENSIVE_LANGUAGE,
    GLUE_COLA,
    GLUE_SST2,
    GO_EMOTIONS,
    IMDB,
    NEWSGROUPS,
    SENTEVAL_CR,
    SENTEVAL_MPQA,
    SENTEVAL_MR,
    SENTEVAL_SST_BINARY,
    SENTEVAL_SST_GRANULAR,
    SENTEVAL_SUBJ,
    SENTIMENT_140,
    STACKOVERFLOW,
    TREC_6,
    TREC_50,
    WASSA_ANGER,
    WASSA_FEAR,
    WASSA_JOY,
    WASSA_SADNESS,
    YAHOO_ANSWERS,
    ClassificationCorpus,
    ClassificationDataset,
    CSVClassificationCorpus,
    CSVClassificationDataset,
)

# word sense disambiguation
# Expose all entity linking datasets
from .entity_linking import (
    CTD_CHEMICALS_DICTIONARY,
    CTD_DISEASES_DICTIONARY,
    NCBI_GENE_HUMAN_DICTIONARY,
    NCBI_TAXONOMY_DICTIONARY,
    NEL_ENGLISH_AIDA,
    NEL_ENGLISH_AQUAINT,
    NEL_ENGLISH_IITB,
    NEL_ENGLISH_REDDIT,
    NEL_ENGLISH_TWEEKI,
    NEL_GERMAN_HIPE,
    WSD_MASC,
    WSD_OMSTI,
    WSD_RAGANATO_ALL,
    WSD_SEMCOR,
    WSD_TRAINOMATIC,
    WSD_UFSAC,
    WSD_WORDNET_GLOSS_TAGGED,
    ZELDA,
    EntityLinkingDictionary,
    HunerEntityLinkingDictionary,
)

# Expose all relation extraction datasets
from .ocr import SROIE, OcrJsonDataset
from .relation_extraction import (
    RE_ENGLISH_CONLL04,
    RE_ENGLISH_DRUGPROT,
    RE_ENGLISH_SEMEVAL2010,
    RE_ENGLISH_TACRED,
)

# universal proposition banks
# keyphrase detection datasets
# other NER datasets
# standard NER datasets
# Expose all sequence labeling datasets
from .sequence_labeling import (
    BIOSCOPE,
    CONLL_03,
    CONLL_03_DUTCH,
    CONLL_03_GERMAN,
    CONLL_03_SPANISH,
    CONLL_2000,
    FEWNERD,
    KEYPHRASE_INSPEC,
    KEYPHRASE_SEMEVAL2010,
    KEYPHRASE_SEMEVAL2017,
    MASAKHA_POS,
    NER_ARABIC_ANER,
    NER_ARABIC_AQMAR,
    NER_BASQUE,
    NER_CHINESE_WEIBO,
    NER_DANISH_DANE,
    NER_ENGLISH_MOVIE_COMPLEX,
    NER_ENGLISH_MOVIE_SIMPLE,
    NER_ENGLISH_PERSON,
    NER_ENGLISH_RESTAURANT,
    NER_ENGLISH_SEC_FILLINGS,
    NER_ENGLISH_STACKOVERFLOW,
    NER_ENGLISH_TWITTER,
    NER_ENGLISH_WEBPAGES,
    NER_ENGLISH_WIKIGOLD,
    NER_ENGLISH_WNUT_2020,
    NER_FINNISH,
    NER_GERMAN_BIOFID,
    NER_GERMAN_EUROPARL,
    NER_GERMAN_GERMEVAL,
    NER_GERMAN_LEGAL,
    NER_GERMAN_MOBIE,
    NER_GERMAN_POLITICS,
    NER_HIPE_2022,
    NER_HUNGARIAN,
    NER_ICDAR_EUROPEANA,
    NER_ICELANDIC,
    NER_JAPANESE,
    NER_MASAKHANE,
    NER_MULTI_CONER,
    NER_MULTI_CONER_V2,
    NER_MULTI_WIKIANN,
    NER_MULTI_WIKINER,
    NER_MULTI_XTREME,
    NER_NERMUD,
    NER_SWEDISH,
    NER_TURKU,
    NER_UKRAINIAN,
    NOISY_NER_EST,
    ONTONOTES,
    UP_CHINESE,
    UP_ENGLISH,
    UP_FINNISH,
    UP_FRENCH,
    UP_GERMAN,
    UP_ITALIAN,
    UP_SPANISH,
    UP_SPANISH_ANCORA,
    WNUT_17,
    ColumnCorpus,
    ColumnDataset,
)

# Expose all text-image datasets
from .text_image import FeideggerCorpus, FeideggerDataset

# Expose all text-text datasets
from .text_text import (
    GLUE_MNLI,
    GLUE_MRPC,
    GLUE_QNLI,
    GLUE_QQP,
    GLUE_RTE,
    GLUE_STSB,
    GLUE_WNLI,
    SUPERGLUE_RTE,
    DataPairCorpus,
    DataPairDataset,
    OpusParallelCorpus,
    ParallelTextCorpus,
    ParallelTextDataset,
)

# Expose all treebanks
from .treebanks import (
    UD_AFRIKAANS,
    UD_ANCIENT_GREEK,
    UD_ARABIC,
    UD_ARMENIAN,
    UD_BASQUE,
    UD_BELARUSIAN,
    UD_BULGARIAN,
    UD_CATALAN,
    UD_CHINESE,
    UD_COPTIC,
    UD_CROATIAN,
    UD_CZECH,
    UD_DANISH,
    UD_DUTCH,
    UD_ENGLISH,
    UD_ESTONIAN,
    UD_FAROESE,
    UD_FINNISH,
    UD_FRENCH,
    UD_GALICIAN,
    UD_GERMAN,
    UD_GERMAN_HDT,
    UD_GOTHIC,
    UD_GREEK,
    UD_HEBREW,
    UD_HINDI,
    UD_INDONESIAN,
    UD_IRISH,
    UD_ITALIAN,
    UD_JAPANESE,
    UD_KAZAKH,
    UD_KOREAN,
    UD_LATIN,
    UD_LATVIAN,
    UD_LITHUANIAN,
    UD_LIVVI,
    UD_MALTESE,
    UD_MARATHI,
    UD_NORTH_SAMI,
    UD_NORWEGIAN,
    UD_OLD_CHURCH_SLAVONIC,
    UD_OLD_FRENCH,
    UD_PERSIAN,
    UD_POLISH,
    UD_PORTUGUESE,
    UD_ROMANIAN,
    UD_RUSSIAN,
    UD_SERBIAN,
    UD_SLOVAK,
    UD_SLOVENIAN,
    UD_SPANISH,
    UD_SWEDISH,
    UD_TURKISH,
    UD_UKRAINIAN,
    UD_WOLOF,
    UniversalDependenciesCorpus,
    UniversalDependenciesDataset,
)

__all__ = [
    "DataLoader",
    "OcrJsonDataset",
    "SROIE",
    "FlairDatapointDataset",
    "SentenceDataset",
    "MongoDataset",
    "StringDataset",
    "EntityLinkingDictionary",
    "AGNEWS",
    "ANAT_EM",
    "AZDZ",
    "BC2GM",
    "BIO_INFER",
    "BIOBERT_CHEMICAL_BC4CHEMD",
    "BIOBERT_CHEMICAL_BC5CDR",
    "BIOBERT_DISEASE_BC5CDR",
    "BIOBERT_DISEASE_NCBI",
    "BIOBERT_GENE_BC2GM",
    "BIOBERT_GENE_JNLPBA",
    "BIOBERT_SPECIES_LINNAEUS",
    "BIOBERT_SPECIES_S800",
    "BIONLP2013_CG",
    "BIONLP2013_PC",
    "BIOSEMANTICS",
    "CDR",
    "CELL_FINDER",
    "CEMP",
    "CHEMDNER",
    "CLL",
    "CRAFT",
    "CRAFT_V4",
    "DECA",
    "FSU",
    "GELLUS",
    "GPRO",
    "HunerEntityLinkingDictionary",
    "HUNER_CELL_LINE",
    "HUNER_CELL_LINE_CELL_FINDER",
    "HUNER_CELL_LINE_CLL",
    "HUNER_CELL_LINE_GELLUS",
    "HUNER_CELL_LINE_JNLPBA",
    "HUNER_CHEMICAL",
    "HUNER_CHEMICAL_CDR",
    "HUNER_CHEMICAL_CEMP",
    "HUNER_CHEMICAL_CHEBI",
    "HUNER_CHEMICAL_CHEMDNER",
    "HUNER_CHEMICAL_CRAFT_V4",
    "HUNER_CHEMICAL_SCAI",
    "HUNER_DISEASE",
    "HUNER_DISEASE_CDR",
    "HUNER_DISEASE_MIRNA",
    "HUNER_DISEASE_NCBI",
    "HUNER_DISEASE_PDR",
    "HUNER_DISEASE_SCAI",
    "HUNER_DISEASE_VARIOME",
    "HUNER_GENE",
    "HUNER_GENE_BC2GM",
    "HUNER_GENE_BIO_INFER",
    "HUNER_GENE_CELL_FINDER",
    "HUNER_GENE_CHEBI",
    "HUNER_GENE_CRAFT_V4",
    "HUNER_GENE_DECA",
    "HUNER_GENE_FSU",
    "HUNER_GENE_GPRO",
    "HUNER_GENE_IEPA",
    "HUNER_GENE_JNLPBA",
    "HUNER_GENE_LOCTEXT",
    "HUNER_GENE_MIRNA",
    "HUNER_GENE_OSIRIS",
    "HUNER_GENE_VARIOME",
    "HUNER_SPECIES",
    "HUNER_SPECIES_CELL_FINDER",
    "HUNER_SPECIES_CHEBI",
    "HUNER_SPECIES_CRAFT_V4",
    "HUNER_SPECIES_LINNEAUS",
    "HUNER_SPECIES_LOCTEXT",
    "HUNER_SPECIES_MIRNA",
    "HUNER_SPECIES_S800",
    "HUNER_SPECIES_VARIOME",
    "IEPA",
    "JNLPBA",
    "LINNEAUS",
    "LOCTEXT",
    "MIRNA",
    "NCBI_GENE_HUMAN_DICTIONARY",
    "NCBI_TAXONOMY_DICTIONARY",
    "CTD_DISEASES_DICTIONARY",
    "CTD_CHEMICALS_DICTIONARY",
    "NCBI_DISEASE",
    "ONTONOTES",
    "OSIRIS",
    "PDR",
    "S800",
    "SCAI_CHEMICALS",
    "SCAI_DISEASE",
    "VARIOME",
    "AMAZON_REVIEWS",
    "COMMUNICATIVE_FUNCTIONS",
    "GERMEVAL_2018_OFFENSIVE_LANGUAGE",
    "GLUE_COLA",
    "GO_EMOTIONS",
    "IMDB",
    "NEWSGROUPS",
    "STACKOVERFLOW",
    "SENTEVAL_CR",
    "SENTEVAL_MPQA",
    "SENTEVAL_MR",
    "SENTEVAL_SST_BINARY",
    "SENTEVAL_SST_GRANULAR",
    "SENTEVAL_SUBJ",
    "SENTIMENT_140",
    "TREC_6",
    "TREC_50",
    "WASSA_ANGER",
    "WASSA_FEAR",
    "WASSA_JOY",
    "WASSA_SADNESS",
    "YAHOO_ANSWERS",
    "ClassificationCorpus",
    "ClassificationDataset",
    "CSVClassificationCorpus",
    "CSVClassificationDataset",
    "NEL_ENGLISH_AIDA",
    "NEL_ENGLISH_AQUAINT",
    "NEL_ENGLISH_IITB",
    "NEL_ENGLISH_REDDIT",
    "NEL_ENGLISH_TWEEKI",
    "NEL_GERMAN_HIPE",
    "WSD_MASC",
    "WSD_OMSTI",
    "WSD_RAGANATO_ALL",
    "WSD_SEMCOR",
    "WSD_TRAINOMATIC",
    "WSD_UFSAC",
    "WSD_WORDNET_GLOSS_TAGGED",
    "RE_ENGLISH_CONLL04",
    "RE_ENGLISH_DRUGPROT",
    "RE_ENGLISH_SEMEVAL2010",
    "RE_ENGLISH_TACRED",
    "BIOSCOPE",
    "CONLL_03",
    "CONLL_03_DUTCH",
    "CONLL_03_GERMAN",
    "CONLL_03_SPANISH",
    "CONLL_2000",
    "FEWNERD",
    "KEYPHRASE_INSPEC",
    "KEYPHRASE_SEMEVAL2010",
    "KEYPHRASE_SEMEVAL2017",
    "MASAKHA_POS",
    "NER_ARABIC_ANER",
    "NER_ARABIC_AQMAR",
    "NER_BASQUE",
    "NER_CHINESE_WEIBO",
    "NER_DANISH_DANE",
    "NER_ENGLISH_MOVIE_COMPLEX",
    "NER_ENGLISH_MOVIE_SIMPLE",
    "NER_ENGLISH_PERSON",
    "NER_ENGLISH_RESTAURANT",
    "NER_ENGLISH_SEC_FILLINGS",
    "NER_ENGLISH_STACKOVERFLOW",
    "NER_ENGLISH_TWITTER",
    "NER_ENGLISH_WEBPAGES",
    "NER_ENGLISH_WIKIGOLD",
    "NER_ENGLISH_WNUT_2020",
    "NER_FINNISH",
    "NER_GERMAN_BIOFID",
    "NER_GERMAN_EUROPARL",
    "NER_GERMAN_GERMEVAL",
    "NER_GERMAN_LEGAL",
    "NER_GERMAN_MOBIE",
    "NER_GERMAN_POLITICS",
    "NER_HIPE_2022",
    "NER_HUNGARIAN",
    "NER_ICDAR_EUROPEANA",
    "NER_ICELANDIC",
    "NER_JAPANESE",
    "NER_NERMUD",
    "NER_MASAKHANE",
    "NER_MULTI_WIKIANN",
    "NER_MULTI_WIKINER",
    "NER_MULTI_XTREME",
    "NER_SWEDISH",
    "NER_TURKU",
    "NER_UKRAINIAN",
    "NOISY_NER_EST",
    "UP_CHINESE",
    "UP_ENGLISH",
    "UP_FINNISH",
    "UP_FRENCH",
    "UP_GERMAN",
    "UP_ITALIAN",
    "UP_SPANISH",
    "UP_SPANISH_ANCORA",
    "WNUT_17",
    "ColumnCorpus",
    "ColumnDataset",
    "NER_MULTI_CONER",
    "NER_MULTI_CONER_V2",
    "FeideggerCorpus",
    "FeideggerDataset",
    "GLUE_MNLI",
    "GLUE_MRPC",
    "GLUE_QNLI",
    "GLUE_QQP",
    "GLUE_RTE",
    "GLUE_WNLI",
    "GLUE_SST2",
    "GLUE_STSB",
    "SUPERGLUE_RTE",
    "DataPairCorpus",
    "DataPairDataset",
    "OpusParallelCorpus",
    "ParallelTextCorpus",
    "ParallelTextDataset",
    "UD_AFRIKAANS",
    "UD_ANCIENT_GREEK",
    "UD_ARABIC",
    "UD_ARMENIAN",
    "UD_BASQUE",
    "UD_BELARUSIAN",
    "UD_BULGARIAN",
    "UD_CATALAN",
    "UD_CHINESE",
    "UD_COPTIC",
    "UD_CROATIAN",
    "UD_CZECH",
    "UD_DANISH",
    "UD_DUTCH",
    "UD_ENGLISH",
    "UD_ESTONIAN",
    "UD_FAROESE",
    "UD_FINNISH",
    "UD_FRENCH",
    "UD_GALICIAN",
    "UD_GERMAN",
    "UD_GERMAN_HDT",
    "UD_GOTHIC",
    "UD_GREEK",
    "UD_HEBREW",
    "UD_HINDI",
    "UD_INDONESIAN",
    "UD_IRISH",
    "UD_ITALIAN",
    "UD_JAPANESE",
    "UD_KAZAKH",
    "UD_KOREAN",
    "UD_LATIN",
    "UD_LATVIAN",
    "UD_LITHUANIAN",
    "UD_LIVVI",
    "UD_MALTESE",
    "UD_MARATHI",
    "UD_NORTH_SAMI",
    "UD_NORWEGIAN",
    "UD_OLD_CHURCH_SLAVONIC",
    "UD_OLD_FRENCH",
    "UD_PERSIAN",
    "UD_POLISH",
    "UD_PORTUGUESE",
    "UD_ROMANIAN",
    "UD_RUSSIAN",
    "UD_SERBIAN",
    "UD_SLOVAK",
    "UD_SLOVENIAN",
    "UD_SPANISH",
    "UD_SWEDISH",
    "UD_TURKISH",
    "UD_UKRAINIAN",
    "UD_WOLOF",
    "UniversalDependenciesCorpus",
    "UniversalDependenciesDataset",
    "ZELDA",
]
