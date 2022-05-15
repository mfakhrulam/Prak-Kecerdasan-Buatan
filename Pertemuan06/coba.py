# from ai_pkg.planning import (HLA, Problem as PlanProblem)
from aima.planning import HLA, RealWorldPlanningProblem

library = {
    'HLA': ['Go(Home,Airport)',
        'Go(Home,Airport)',
        'Drive(Home, AirportParking)',
        'Shuttle(AirportParking, Airport)',
        'Taxi(Home, Airport)'],
    'steps':[['Drive(Home, AirportParking)','Shuttle(AirportParking, Airport)'],
        ['Taxi(Home, Airport)'],
        [],
        [],
        []],
    'precond': [['At(Home) & Have(Car)'],
        ['At(Home)'],
        ['At(Home) & Have(Car)'],
        ['At(AirportParking)'],
        ['At(Home)']],
    'effect': [['At(Airport) & ~At(Home)'],
        ['At(Airport) & ~At(Home) & ~Have(Cash)'],
        ['At(AirportParking) & ~At(Home)'],
        ['At(Airport) & ~At(AirportParking)'],
        ['At(Airport) & ~At(Home) & ~Have(Cash)']]
}

goto_airport = HLA('Go(Home, Airport)', precond='At(Home)', effect='At(Airport) & ~At(Home)')
taxi_airport = HLA('Taxi(Home,Airport)', precond='At(Home)', effect='At(Airport) & ~At(Home) & ~Have(Cash)')
drive_AirportParking = HLA('Drive(Home, AirportParking)', 'At(Home) & Have(Car)','At(LongTermParking) & ~At(Home)' )
shuttle_SFO = HLA('Shuttle(AirportParking, SFO)', 'At(AirportParking)', 'At(SFO) & ~At(LongTermParking)')
problem = RealWorldPlanningProblem('At(Home) & Have(Cash) & Have(Car) ', 'At(Airport) & Have(Cash)', [goto_airport])
plan = problem.hierarchical_search(library)

print('--- Get to SFO1 problem ---')
# print (plan, '\n')
# print ([x.__dict__ for x in plan])
# print()
for i in range(0, len(plan)):
    print('precondition: ', plan[i].precond)
    print('action: ' , plan[i].name, plan[i].args)
    print('effect : ', plan[i].effect)
    print()

library = {
        'HLA': ['Go(Home,SFO)', 
            'Go(Home,SFO)', 
            'Drive(Home, SFOLongTermParking)', 
            'Shuttle(SFOLongTermParking, SFO)', 
            'Taxi(Home, SFO)'],
        'steps': [['Drive(Home, SFOLongTermParking)', 'Shuttle(SFOLongTermParking, SFO)'],
            ['Taxi(Home, SFO)'],
            [], 
            [], 
            []],
        'precond': [['At(Home) & Have(Car)'],
            ['At(Home)'], 
            ['At(Home) & Have(Car)'], 
            ['At(SFOLongTermParking)'], 
            ['At(Home)']],
        'effect': [['At(SFO) & ~At(Home)'], 
            ['At(SFO) & ~At(Home) & ~Have(Cash)'], 
            ['At(SFOLongTermParking) & ~At(Home)'], 
            ['At(SFO) & ~At(LongTermParking)'], 
            ['At(SFO) & ~At(Home) & ~Have(Cash)']] }
# # Possible actions
# go_SFO = HLA('Go(Home,SFO)', precond='At(Home)', effect='At(SFO) & ~At(Home)')
# taxi_SFO = HLA('Taxi(Home,SFO)', precond='At(Home)', effect='At(SFO) & ~At(Home) & ~Have(Cash)')
# drive_SFOLongTermParking = HLA('Drive(Home, SFOLongTermParking)', 'At(Home) & Have(Car)','At(SFOLongTermParking) & ~At(Home)' )
# shuttle_SFO = HLA('Shuttle(SFOLongTermParking, SFO)', 'At(SFOLongTermParking)', 'At(SFO) & ~At(LongTermParking)')
# # Create a problem
# problem = RealWorldPlanningProblem('At(Home) & Have(Cash) & Have(Car)', 'At(SFO) & Have(Cash)', [go_SFO])
# # Hierarchical Search
# plan = problem.hierarchical_search(library)
#  print('--- Get to SFO1 problem ---')
#     print (plan, '\n')
#     print ([x.__dict__ for x in plan])
#     print()



# prak
# goto_airport = HLA('Go(Home, Airport)', precond='At(Home)', effect='At(Airport) & ~At(Home)')
# problem = PlanProblem('At(Home) & Have(Cash) & Have(Car) ', 'At(Airport) & Have(Cash)', [goto_airport])

# solution = PlanProblem.hierarchical_search(problem, library)
# for i in range(0, len(solution)):
#     print('precondition: ', solution[i].precond)
#     print('action: ' , solution[i].name, solution[i].args)
#     print('effect : ', solution[i].effect)