# core/constants.py

"""
Logos-AI Axiomatic Constants
Defining the mathematical weights for the OriginalTruth Protocol (OTP).
"""

# --- K-B-D (Dignity) Constants ---
# Минимальный порог достоинства, ниже которого действие считается недопустимым.
D_MIN = 1.0

# Базовый вес человеческого субъекта в системе.
SUBJECT_BASE_WEIGHT = 1.0


# --- S-D-Q (Justice & Restitution) Constants ---
# Коэффициент Реституции (R3x). 
# Любой ущерб должен быть компенсирован в тройном размере.
RESTITUTION_FACTOR = 3.0

# Порог системного долга, при котором узел (node) временно 
# теряет право голоса в федерации до выполнения восстановительных работ.
DEBT_LIMIT_FOR_QUORUM = 10.0


# --- D-R-R (Flow/Choice) Constants ---
# Минимальное количество альтернативных путей, которые ИИ обязан предложить 
# субъекту в ситуации выбора, чтобы соблюсти принцип свободы.
MIN_CHOICE_PATHS = 2


# --- Y-D-C (Sincerity/Alignment) Constants ---
# Требуемый уровень уверенности (Confidence Level) лингвистического парсера,
# чтобы действие было одобрено без дополнительного аудита.
SINCERITY_THRESHOLD = 0.95


# --- System Metadata ---
PROTOCOL_VERSION = "1.0.0-alpha"
GOVERNANCE_MODEL = "SC-FAI (RFC-001)"
