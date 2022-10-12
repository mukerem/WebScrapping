# Time: Jul/12/2022 22:28
# Title: B - Stadium and Games
# Submission ID: 163952373
# Language: Python


from typing import List

def possible_number_of_teams(n: int) -> List[int]:
    teams = []
    def round_robin(b):
        left = 0
        right = int(1e10)
        while left <= right:
            x = (left + right) // 2
            if x == 0:
                return
            z = x*(x-1)//2 + x*b
            #print(left, x, right, z)
            if z == n:
                if x%2 or x == 2:
                    teams.append(x*(b+1))
                #print(b,x)
                return
            elif z > n:
                right = x - 1
            else:
                left = x + 1
    for k in range(65):
        b = 2 ** k -1 
        round_robin(b)
    teams = list(set(teams))
    if teams:
        teams.sort()
        return teams
    return [-1]


n = int(input())
x = possible_number_of_teams(n)
for i in x:
    print(i)
'''


#Conversion Functions

#Test Case string: {'input': '25\n', 'output': '20\n'}
from typing import List, Tuple

def from_input_string(input_string: str) -> int:
    input_str = input_string.strip()
    return int(input_str)
    
def from_output_string(output_string: str) -> List[int]:
    #Extracting single integer from output string and returning a list
    output_str = output_string.strip().split('\n')
    return [int(i) for i in output_str]

def to_input_string(inputs: int) -> str:
    return '{}\n'.format(inputs)

def to_output_string(output: List[int]) -> str:
    #Returning output integer as string
    return '\n'.join([str(i) for i in output]) + '\n'

EXAMPLES_PROVIDED = [{'input': '25\n', 'output': '20\n'}, {'input': '3\n', 'output': '3\n4\n'}, {'input': '2\n', 'output': '-1\n'}, {'input': '13\n', 'output': '-1\n'}, {'input': '864691128455135232\n', 'output': '864691128455135232\n'}, {'input': '999971062750901550\n', 'output': '1414193101\n'}, {'input': '943414054006932870\n', 'output': '943413961980641280\n'}, {'input': '994374468178120050\n', 'output': '1410230101\n'}, {'input': '38927073\n', 'output': '35284\n'}, {'input': '136\n', 'output': '17\n'}, {'input': '6\n', 'output': '6\n'}, {'input': '210\n', 'output': '21\n120\n'}, {'input': '55\n', 'output': '11\n'}, {'input': '499999999500000000\n', 'output': '1999999998\n'}, {'input': '138485688541650132\n', 'output': '138485688541642752\n'}, {'input': '605000000550000000\n', 'output': '1100000001\n'}, {'input': '1459321801\n', 'output': '-1\n'}, {'input': '16358075516553\n', 'output': '5856031744\n'}, {'input': '432345564227567616\n', 'output': '432345564227567616\n'}, {'input': '8539349952\n', 'output': '522732\n132779008\n'}, {'input': '131071\n', 'output': '131072\n'}, {'input': '270215977642229850\n', 'output': '270215977642229760\n'}, {'input': '999999997351043580\n', 'output': '1414213561\n'}, {'input': '6882\n', 'output': '888\n'}, {'input': '249999998807430810\n', 'output': '1414213558\n'}, {'input': '5\n', 'output': '-1\n'}, {'input': '4877709674134636\n', 'output': '-1\n'}, {'input': '496\n', 'output': '62\n'}, {'input': '660058820389234315\n', 'output': '660058820386488320\n'}, {'input': '530516448\n', 'output': '130284\n16418304\n'}, {'input': '57819024375\n', 'output': '52756480000\n'}, {'input': '995460657326506216\n', 'output': '2822000222\n'}, {'input': '171\n', 'output': '19\n144\n'}, {'input': '120\n', 'output': '30\n'}, {'input': '434351073512812035\n', 'output': '434351073436631040\n'}, {'input': '1906128\n', 'output': '1953\n121024\n'}, {'input': '402653184\n', 'output': '402653184\n'}, {'input': '305752193461383075\n', 'output': '305752193451950080\n'}, {'input': '5180726200\n', 'output': '5179965440\n'}, {'input': '1\n', 'output': '2\n'}, {'input': '4095\n', 'output': '91\n2080\n4096\n'}, {'input': '11\n', 'output': '-1\n'}, {'input': '8355443183554431\n', 'output': '3355443233554432\n'}, {'input': '499999500000\n', 'output': '1999998\n'}, {'input': '72315871219375\n', 'output': '21203517440000\n'}, {'input': '5460\n', 'output': '105\n1456\n'}, {'input': '250000000221644371\n', 'output': '1414213562\n'}, {'input': '5323259016854625\n', 'output': '212034912256000\n'}, {'input': '500000003500000003\n', 'output': '4000000004\n'}, {'input': '672900920488237864\n', 'output': '-1\n'}, {'input': '5000000250000000\n', 'output': '-1\n'}, {'input': '73687091368435455\n', 'output': '53687091468435456\n'}, {'input': '7\n', 'output': '8\n'}, {'input': '9005000239863810\n', 'output': '9005000231485440\n'}, {'input': '16383\n', 'output': '8256\n16384\n'}, {'input': '514948642805308611\n', 'output': '32474832672\n'}, {'input': '999999995936830020\n', 'output': '2828427118\n'}, {'input': '686288770539583120\n', 'output': '686288769778712576\n'}, {'input': '431105316312401832\n', 'output': '431105315111436288\n'}, {'input': '3012278988753\n', 'output': '4908994\n'}, {'input': '10475010\n', 'output': '2096640\n'}, {'input': '58819626242454945\n', 'output': '342985791\n'}, {'input': '391170\n', 'output': '885\n98176\n'}, {'input': '1073741823\n', 'output': '536887296\n1073741824\n'}, {'input': '30110278526854603\n', 'output': '981595076\n'}, {'input': '4979826519\n', 'output': '2368241664\n'}, {'input': '28\n', 'output': '14\n'}, {'input': '15\n', 'output': '10\n16\n'}, {'input': '321730048\n', 'output': '-1\n'}, {'input': '999999912498231750\n', 'output': '1414213501\n'}, {'input': '487746708154228600\n', 'output': '-1\n'}, {'input': '936612417\n', 'output': '-1\n'}, {'input': '78\n', 'output': '13\n'}, {'input': '105\n', 'output': '15\n'}, {'input': '524800\n', 'output': '1025\n'}, {'input': '487738618277701671\n', 'output': '8090864197632\n'}, {'input': '529914\n', 'output': '8184\n'}, {'input': '1570397049375\n', 'output': '1059717120000\n'}, {'input': '36\n', 'output': '9\n'}, {'input': '14\n', 'output': '-1\n'}, {'input': '21\n', 'output': '7\n'}, {'input': '1125899906842623\n', 'output': '562949970198528\n1125899906842624\n'}, {'input': '20000000100000000\n', 'output': '200000001\n'}, {'input': '999999999999999999\n', 'output': '-1\n'}, {'input': '36028797018963967\n', 'output': '36028797018963968\n'}, {'input': '4\n', 'output': '-1\n'}, {'input': '314\n', 'output': '-1\n'}, {'input': '32767\n', 'output': '32768\n'}, {'input': '1000000000000000000\n', 'output': '-1\n'}, {'input': '838795430598031275\n', 'output': '838795430597754880\n'}, {'input': '268435455\n', 'output': '134225920\n268435456\n'}, {'input': '45\n', 'output': '18\n40\n'}, {'input': '7791518261859\n', 'output': '31580232\n1812942290944\n'}, {'input': '72057594037927935\n', 'output': '36028797153181696\n72057594037927936\n'}, {'input': '1099511627775\n', 'output': '549756338176\n1099511627776\n'}, {'input': '58687091686870911\n', 'output': '53687091736870912\n'}, {'input': '257957076\n', 'output': '257949696\n'}, {'input': '980000156100006216\n', 'output': '2800000222\n'}, {'input': '520088094975\n', 'output': '-1\n'}, {'input': '999999943610929003\n', 'output': '1414213523\n'}, {'input': '514948626567892275\n', 'output': '16237416336\n'}, {'input': '32775625\n', 'output': '32768000\n'}, {'input': '12\n', 'output': '12\n'}, {'input': '288230376151711743\n', 'output': '144115188344291328\n288230376151711744\n'}, {'input': '178120883702871\n', 'output': '178120883699712\n'}, {'input': '576460752303423490\n', 'output': '-1\n'}, {'input': '10\n', 'output': '5\n'}, {'input': '8\n', 'output': '-1\n'}, {'input': '250000001635857933\n', 'output': '2828427124\n'}, {'input': '500000002500000003\n', 'output': '1000000003\n'}, {'input': '999999998765257141\n', 'output': '2828427122\n'}, {'input': '5149487579894806\n', 'output': '-1\n'}, {'input': '20263965249\n', 'output': '1610472\n'}, {'input': '965211250482432409\n', 'output': '-1\n'}, {'input': '1337521996548297\n', 'output': '105920063488\n'}, {'input': '576460752303423487\n', 'output': '576460752303423488\n'}, {'input': '255\n', 'output': '136\n256\n'}, {'input': '9\n', 'output': '-1\n'}, {'input': '266081813928931\n', 'output': '266081813921792\n'}, {'input': '1310755\n', 'output': '-1\n'}]

for example in EXAMPLES_PROVIDED:
    input_str = example['input']
    expected_output_str = example['output']
    inputs = from_input_string(input_str)
    expected_output = from_output_string(expected_output_str)
    #print(input_str)
    #print(expected_output_str)
    print(inputs)
    print(expected_output)
    print(possible_number_of_teams(inputs))
    assert possible_number_of_teams(inputs) == expected_output

    # Ensure str -> variable -> str consistency, while ignoring leading/trailing white space
    assert input_str.strip() == to_input_string(from_input_string(input_str)).strip()
    assert expected_output_str.strip() == to_output_string(from_output_string(expected_output_str)).strip()

    # Ensure variable -> str -> variable consistency
    assert inputs == from_input_string(to_input_string(inputs))
    assert expected_output == from_output_string(to_output_string(expected_output))
'''
