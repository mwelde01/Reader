"""
Reading Level Standards and Pedagogical Framework
Based on Guided Reading Levels, Lexile Framework, and Common Core Standards
"""

READING_LEVELS = {
    "Pre-K (Emergent Reader)": {
        "guided_reading": "A-C",
        "grade_equivalent": "Pre-K to K",
        "lexile": "BR (Beginning Reader)",
        "characteristics": {
            "words_per_page": "1-3",
            "sentences": "Simple, repetitive patterns",
            "vocabulary": "High-frequency words, basic nouns and verbs",
            "concepts": "Familiar objects and experiences",
            "sentence_structure": "Simple subject-verb or subject-verb-object"
        },
        "pedagogy": {
            "focus": "Print awareness, one-to-one correspondence, directionality",
            "support": "Picture support on every page, predictable text patterns",
            "skills": "Letter recognition, phonemic awareness, basic sight words"
        }
    },
    "Kindergarten": {
        "guided_reading": "D-E",
        "grade_equivalent": "K to 1st",
        "lexile": "BR to 200L",
        "characteristics": {
            "words_per_page": "4-6",
            "sentences": "Short, simple sentences with occasional compound sentences",
            "vocabulary": "Familiar words, basic descriptive words",
            "concepts": "Everyday experiences, simple story plots",
            "sentence_structure": "Subject-verb-object with simple conjunctions"
        },
        "pedagogy": {
            "focus": "Decoding CVC words, building sight word vocabulary",
            "support": "Strong picture support, repetitive language patterns",
            "skills": "Beginning phonics, basic comprehension, retelling"
        }
    },
    "1st Grade": {
        "guided_reading": "F-I",
        "grade_equivalent": "1st",
        "lexile": "200L to 400L",
        "characteristics": {
            "words_per_page": "7-15",
            "sentences": "Longer sentences, some complex structures",
            "vocabulary": "Expanded vocabulary, some content-specific words",
            "concepts": "Simple narratives with clear beginning, middle, end",
            "sentence_structure": "Varied sentence beginnings, compound sentences"
        },
        "pedagogy": {
            "focus": "Fluency development, comprehension strategies",
            "support": "Pictures support meaning, less predictable text",
            "skills": "Phonics patterns, sight words, basic inference"
        }
    },
    "2nd Grade": {
        "guided_reading": "J-M",
        "grade_equivalent": "2nd",
        "lexile": "400L to 600L",
        "characteristics": {
            "words_per_page": "15-30",
            "sentences": "More complex sentences with dialogue",
            "vocabulary": "Growing vocabulary, some academic language",
            "concepts": "Multi-chapter books, character development",
            "sentence_structure": "Complex sentences with multiple clauses"
        },
        "pedagogy": {
            "focus": "Reading comprehension, text analysis",
            "support": "Some illustrations, chapter divisions",
            "skills": "Fluency, comprehension strategies, making connections"
        }
    },
    "3rd Grade": {
        "guided_reading": "N-P",
        "grade_equivalent": "3rd",
        "lexile": "600L to 800L",
        "characteristics": {
            "words_per_page": "30-50",
            "sentences": "Varied sentence structures, descriptive language",
            "vocabulary": "Academic vocabulary, figurative language introduced",
            "concepts": "Multiple plots/subplots, character complexity",
            "sentence_structure": "Complex and compound-complex sentences"
        },
        "pedagogy": {
            "focus": "Independent reading, critical thinking",
            "support": "Fewer illustrations, longer chapters",
            "skills": "Inference, theme identification, analysis"
        }
    },
    "4th Grade": {
        "guided_reading": "Q-S",
        "grade_equivalent": "4th",
        "lexile": "800L to 950L",
        "characteristics": {
            "words_per_page": "50-100",
            "sentences": "Sophisticated sentence structures",
            "vocabulary": "Content-specific vocabulary, idioms",
            "concepts": "Abstract concepts, multiple perspectives",
            "sentence_structure": "Varied for effect, complex structures"
        },
        "pedagogy": {
            "focus": "Analytical reading, text-to-text connections",
            "support": "Minimal illustrations, chapter books",
            "skills": "Analysis, synthesis, evaluation"
        }
    },
    "5th Grade and Above": {
        "guided_reading": "T-Z",
        "grade_equivalent": "5th+",
        "lexile": "950L to 1300L+",
        "characteristics": {
            "words_per_page": "100+",
            "sentences": "Mature, sophisticated writing",
            "vocabulary": "Advanced academic vocabulary, figurative language",
            "concepts": "Complex themes, symbolism, multiple storylines",
            "sentence_structure": "Full range of sentence structures"
        },
        "pedagogy": {
            "focus": "Critical analysis, literary devices",
            "support": "Text-dependent reading",
            "skills": "Advanced analysis, argumentation, synthesis"
        }
    }
}


def get_level_info(level_name):
    """Get detailed information about a reading level"""
    return READING_LEVELS.get(level_name, None)


def get_all_levels():
    """Get list of all available reading levels"""
    return list(READING_LEVELS.keys())


def get_writing_guidelines(level_name):
    """Get specific writing guidelines for creating content at this level"""
    level = READING_LEVELS.get(level_name)
    if not level:
        return None

    return {
        "guided_reading_level": level["guided_reading"],
        "grade": level["grade_equivalent"],
        "lexile": level["lexile"],
        "words_per_page": level["characteristics"]["words_per_page"],
        "sentence_style": level["characteristics"]["sentences"],
        "vocabulary_level": level["characteristics"]["vocabulary"],
        "concept_complexity": level["characteristics"]["concepts"],
        "pedagogical_focus": level["pedagogy"]["focus"],
        "support_features": level["pedagogy"]["support"]
    }
