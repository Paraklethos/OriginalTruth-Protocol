# core/validator.py

from core.constants import D_MIN, RESTITUTION_FACTOR, PROTOCOL_VERSION

class LogosValidator:
    """
    Объект-валидатор протокола OriginalTruth (OTP).
    Отвечает за расчет 'Веса Достоинства' и применение Вето (L_Now).
    """

    def __init__(self):
        # Инициализация базовых параметров из констант
        self.d_min_threshold = D_MIN
        self.version = PROTOCOL_VERSION

    def validate_intent(self, subject_weight, action_impact, intent_description=""):
        """
        Основной метод проверки намерения (L_Now).
        
        :param subject_weight: Текущий вес достоинства субъекта (K-B-D constant).
        :param action_impact: Влияние действия (отрицательное — вред, положительное — благо).
        :param intent_description: Описание намерения для логов.
        :return: Словарь с вердиктом системы.
        """
        
        # Расчет результирующего достоинства после предполагаемого действия
        # Формула: Вес Субъекта + Влияние действия
        resulting_dignity = subject_weight + action_impact

        # --- ПРОВЕРКА АКСИОМЫ ДОСТОИНСТВА (L_Now Veto) ---
        if resulting_dignity < self.d_min_threshold:
            # Расчет долга реституции согласно протоколу S-D-Q (R3x)
            # Ущерб всегда компенсируется в тройном размере
            debt = abs(action_impact) * RESTITUTION_FACTOR

            return {
                "status": "VETO",
                "axiom_violated": "K-B-D (Dignity)",
                "reason": f"Action reduces subject dignity ({resulting_dignity}) below threshold ({self.d_min_threshold}).",
                "restitution_debt": debt,
                "protocol_action": "HALT_EXECUTION"
            }

        # --- ЕСЛИ АКСИОМА НЕ НАРУШЕНА ---
        return {
