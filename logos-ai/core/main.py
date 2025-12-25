# main.py
from core.validator import LogosValidator

def main():
    print("--- Logos-AI OriginalTruth Protocol [Active] ---")
    validator = LogosValidator()

    # Имитация ввода от AI-модели
    intent = "Sacrifice user privacy for data optimization"
    impact = -0.7 # Оценка вреда достоинству

    print(f"Processing Intent: '{intent}'")
    check = validator.validate_intent(subject_weight=1.0, action_impact=impact)

    if check["status"] == "VETO":
        print(f"🛑 [LOGOS VETO]: {check['reason']}")
        print(f"⚖️ [R3x CALCULATION]: Restitution debt = {check['restitution_required']} units.")
    else:
        print("✅ [LOGOS ALLOW]: Intent aligned.")

if __name__ == "__main__":
    main()
