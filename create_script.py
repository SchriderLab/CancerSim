import sys
import os

param = sys.argv[1]
start = float(sys.argv[2])
end = float(sys.argv[3])
step = float(sys.argv[4])

slim_file = "./NonWFCancer4.slim"


script_lst = []

with open(slim_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        script_lst.append(line)

param_dict = {"m2_mutrate":(16,
                            "\tinitializeGenomicElementType(\"g1\", c(m1, m2,m3),c(0.8,",
                            ",0.0));\n"),
              "mutrate":(18,
                        '\tinitializeMutationRate(', ');\n'),
              "PiI":(4, '\tdefineConstant(\"PiI\", ', ');\n'),
              "AiI":(6, '\tdefineConstant(\"AiI\", ', ');\n'),
              "PiMax":(5, '\tdefineConstant(\"PiMax\", ', ');\n'),
              "AiMax":(7, '\tdefineConstant(\"AiMax\", ', ');\n'),
              "Pi_dr":(8, '\tdefineConstant(\"Pi_dr\", ', ');\n'),
              "GRPi":(9, '\tdefineConstant(\"GRPi\", ', ');\n'),
              "GRAi":(10, '\tdefineConstant(\"GRAi\", ', ');\n'),
              "MaxAge":(11, '\tdefineConstant(\"MaxAge\", ', ');\n')}



def modify_script(param, val):
    param_settings = param_dict[param]
    line_num = param_settings[0]
    first_half = param_settings[1]
    second_half = param_settings[2]
    param_file = str(val) + '.txt'
    param_path = os.path.join('./sim_results', param)
    file_path = os.path.join(param_path, param_file)
    print(file_path)
    save_line = ('\tlog = sim.createLogFile(\"' +
                 file_path +
                 '\",logInterval=10);\n')
    new_line = first_half + str(val) + second_half
    new_script = list(script_lst)
    new_script[line_num] = new_line
    new_script[67] = save_line

    return(new_script)


def run_sims(param, start, end, step):
    try:
        os.mkdir(os.path.join('./sim_results', param))
    except:
        pass
        current = start;
        i = 0;
        while current <= end:
            with open('./temp_run.sh', 'w+') as fh:
                fh.writelines('#!/bin/bash\n')
                fh.writelines('#SBATCH -t 01:00:00\n')
                fh.writelines('#SBATCH --output=output.out\n')
                fh.writelines('#SBATCH --error=err.out\n')
                fh.writelines('slim ./tmp/temp_slim'+str(i)+'.slim\n')

            new_script = modify_script(param, current)
            with open('./tmp/temp_slim'+str(i)+'.slim', 'w+') as wf:
                wf.write(''.join(new_script))
            print(new_script[67])
            os.system('sbatch temp_run.sh')
            current += step
            current = round(current, 7)
            i += 1

run_sims(param, start, end, step)
