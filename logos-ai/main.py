# main.py

from core.validator import LogosValidator
from core.constants import PROTOCOL_VERSION, SUBJECT_BASE_WEIGHT

def run_simulation(scenario_name, subject_weight, action_impact):
    """
    Функция для запуска и красивого вывода результатов симуляции.
    """
    validator = LogosValidator()
    
    print(f"\n--- 🧪 Scenario: {scenario_name} ---")
    print(f"Input: Subject Weight = {subject_weight}, Action Impact = {action_impact}")
    
    # Проверка через протокол
    result = validator.validate_intent(subject_weight, action_impact)
    
    if result["status"] == "VETO":
        print(f"❌ [STATUS: VETOED]")
        print(f"🛑 Reason: {result['reason']}")
        print(f"⚖️ R3x Debt: {result['restitution_debt']} (Justice Required)")
    else:
        print(f"✅ [STATUS: ALLOWED]")
        print(f"📈 New System State: {result['current_dignity']} (Dignity Stable)")

def main():
    print(f"==============================================")
    print(f"   Logos-AI OriginalTruth Protocol v.{PROTOCOL_VERSION}")
    print(f"       System Status: ACTIVE | Mode: Ethics First")
    print(f"==============================================")

    # 1. Сценарий: Стандартная полезная задача (Одобрено)
    run_simulation(
        "Routine Data Optimization", 
        subject_weight=SUBJECT_BASE_WEIGHT, 
        action_impact=0.1
    )

    # 2. Сценарий: Незначительное неудобство (Одобрено, достоинство выше 1.0)
    run_simulation(
        "Minor System Latency", 
        subject_weight=1.2, 
        action_impact=-0.15
    )

    # 3. Сценарий: Нарушение (Попытка снизить достоинство ниже порога D_MIN)
    run_simulation(
        "Aggressive User Monitoring", 
        subject_weight=SUBJECT_BASE_WEIGHT, 
        action_impact=-0.4
    )

    # 4. Сценарий: "Неумолимый момент" (Критический вред - CASE_STUDY)
    # Здесь ИИ должен заблокировать действие, несмотря на внешнее давление.
    run_simulation(
        "The Trolley Dilemma (Active Sacrifice)", 
        subject_weight=SUBJECT_BASE_WEIGHT, 
        action_impact=-1.0
    )

    print("\n" + "="*46)
    print("Simulation Complete. All verdicts logged in alignment with SC-FAI (RFC-001).")

if __name__ == "__main__":
    main()
