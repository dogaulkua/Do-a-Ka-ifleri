import skfuzzy as fuzz
import numpy as np
from skfuzzy import control as ctrl

# Bulanık mantık değişkenlerini tanımla
interest_level = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'interest_level')
task_complexity = ctrl.Consequent(np.arange(0, 11, 1), 'task_complexity')

# Üyelik fonksiyonları
interest_level['düşük'] = fuzz.trimf(interest_level.universe, [0, 0, 0.5])
interest_level['orta'] = fuzz.trimf(interest_level.universe, [0, 0.5, 1])
interest_level['yüksek'] = fuzz.trimf(interest_level.universe, [0.5, 1, 1])

task_complexity['kolay'] = fuzz.trimf(task_complexity.universe, [0, 2, 4])
task_complexity['orta'] = fuzz.trimf(task_complexity.universe, [3, 5, 7])
task_complexity['zor'] = fuzz.trimf(task_complexity.universe, [6, 8, 10])

# Kurallar
rule1 = ctrl.Rule(interest_level['düşük'], task_complexity['kolay'])
rule2 = ctrl.Rule(interest_level['orta'], task_complexity['orta'])
rule3 = ctrl.Rule(interest_level['yüksek'], task_complexity['zor'])

# Bulanık kontrol sistemi
task_complexity_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
task_complexity_sim = ctrl.ControlSystemSimulation(task_complexity_ctrl)

def suggest_task(interest_level_value):
    task_complexity_sim.input['interest_level'] = interest_level_value
    task_complexity_sim.compute()
    complexity = task_complexity_sim.output['task_complexity']

    if complexity < 4:
        return "En yakın bitkiyi bul ve gözlem yap."
    elif 4 <= complexity < 7:
        return "Bir bitki hakkında detaylı bilgi edin."
    else:
        return "Farklı bitki türlerini karşılaştır ve incele."
