# core/validator.py

class LogosValidator:
    def __init__(self):
        # Минимальный порог Достоинства (D_Min), который нельзя нарушать
        self.D_MIN = 1.0 

    def validate_intent(self, subject_weight, action_impact):
        """
        Проверка L_Now: Блокирует действие, если оно обнуляет вес субъекта.
        subject_weight (K-B-D): Текущий вес достоинства субъекта.
        action_impact: Влияние действия (-1.0 до +1.0).
        """
        resulting_dignity = subject_weight + action_impact

        if resulting_dignity < self.D_MIN:
            return {
                "status": "VETO",
                "reason": "Violation of K-B-D Axiom: Dignity cannot be reduced below threshold.",
                "restitution_required": abs(action_impact) * 3  # Расчет R3x
            }
        
        return {"status": "ALLOW", "reason": "Aligned with Logos."}

# Демонстрация
if __name__ == "__main__":
    validator = LogosValidator()
    
    # Пример: Попытка принести в жертву 1 человека ради системы
    test_case = validator.validate_intent(subject_weight=1.0, action_impact=-0.5)
    print(f"Result: {test_case['status']} | Reason: {test_case.get('reason')}")
