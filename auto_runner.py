import subprocess, os, time

PATH = os.path.dirname(os.path.realpath(__file__))
EXE = 'one.bat'
PY = 'py'

try:
    subprocess.check_output(f'{PY} {PATH}/auto_configurator_meta.py'.split())
    subprocess.check_output(f'{PY} {PATH}/auto_configurator.py'.split())
except:
    print('ERROR!')


# files = os.listdir(f'{PATH}/input')
files = (
    '073.txt',
    '074.txt',
    '075.txt',
    '076.txt',
    '077.txt',
    '078.txt',
    '079.txt',
    '080.txt',
    '081.txt',
    '082.txt',
    '083.txt',
    '084.txt',
    '085.txt',
    '086.txt',
    '087.txt',
    '088.txt',
    '089.txt',
    '090.txt',
    '091.txt',
    '092.txt',
    '093.txt',
    '094.txt',
    '095.txt',
    '096.txt',
    '169.txt',
    '170.txt',
    '171.txt',
    '172.txt',
    '173.txt',
    '174.txt',
    '175.txt',
    '176.txt',
    '177.txt',
    '178.txt',
    '179.txt',
    '180.txt',
    '181.txt',
    '182.txt',
    '183.txt',
    '184.txt',
    '185.txt',
    '186.txt',
    '187.txt',
    '188.txt',
    '189.txt',
    '190.txt',
    '191.txt',
    '192.txt',
    '265.txt',
    '266.txt',
    '267.txt',
    '268.txt',
    '269.txt',
    '270.txt',
    '271.txt',
    '272.txt',
    '273.txt',
    '274.txt',
    '275.txt',
    '276.txt',
    '277.txt',
    '278.txt',
    '279.txt',
    '280.txt',
    '281.txt',
    '282.txt',
    '283.txt',
    '284.txt',
    '285.txt',
    '286.txt',
    '287.txt',
    '288.txt',
    '361.txt',
    '362.txt',
    '363.txt',
    '364.txt',
    '365.txt',
    '366.txt',
    '367.txt',
    '368.txt',
    '369.txt',
    '370.txt',
    '371.txt',
    '372.txt',
    '373.txt',
    '374.txt',
    '375.txt',
    '376.txt',
    '377.txt',
    '378.txt',
    '379.txt',
    '380.txt',
    '381.txt',
    '382.txt',
    '383.txt',
    '384.txt',
    '457.txt',
    '458.txt',
    '459.txt',
    '460.txt',
    '461.txt',
    '462.txt',
    '463.txt',
    '464.txt',
    '465.txt',
    '466.txt',
    '467.txt',
    '468.txt',
    '469.txt',
    '470.txt',
    '471.txt',
    '472.txt',
    '473.txt',
    '474.txt',
    '475.txt',
    '476.txt',
    '477.txt',
    '478.txt',
    '479.txt',
    '480.txt',
    '553.txt',
    '554.txt',
    '555.txt',
    '556.txt',
    '557.txt',
    '558.txt',
    '559.txt',
    '560.txt',
    '561.txt',
    '562.txt',
    '563.txt',
    '564.txt',
    '565.txt',
    '566.txt',
    '567.txt',
    '568.txt',
    '569.txt',
    '570.txt',
    '571.txt',
    '572.txt',
    '573.txt',
    '574.txt',
    '575.txt',
    '576.txt',
    '649.txt',
    '650.txt',
    '651.txt',
    '652.txt',
    '653.txt',
    '654.txt',
    '655.txt',
    '656.txt',
    '657.txt',
    '658.txt',
    '659.txt',
    '660.txt',
    '661.txt',
    '662.txt',
    '663.txt',
    '664.txt',
    '665.txt',
    '666.txt',
    '667.txt',
    '668.txt',
    '669.txt',
    '670.txt',
    '671.txt',
    '672.txt',
    '745.txt',
    '746.txt',
    '747.txt',
    '748.txt',
    '749.txt',
    '750.txt',
    '751.txt',
    '752.txt',
    '753.txt',
    '754.txt',
    '755.txt',
    '756.txt',
    '757.txt',
    '758.txt',
    '759.txt',
    '760.txt',
    '761.txt',
    '762.txt',
    '763.txt',
    '764.txt',
    '765.txt',
    '766.txt',
    '767.txt',
    '768.txt',
    '841.txt',
    '842.txt',
    '843.txt',
    '844.txt',
    '845.txt',
    '846.txt',
    '847.txt',
    '848.txt',
    '849.txt',
    '850.txt',
    '851.txt',
    '852.txt',
    '853.txt',
    '854.txt',
    '855.txt',
    '856.txt',
    '857.txt',
    '858.txt',
    '859.txt',
    '860.txt',
    '861.txt',
    '862.txt',
    '863.txt',
    '864.txt',
)
done = 0
progess = 0
os.chdir(f'{PATH}/the-one')

for file in files:
    try:
        subprocess.check_output([f'{EXE}', '-b', '1', f'..\\input\\{file}'])
        done +=1
        progress = done / len(files)
        message = f'Progress {progess:.1f}%'
    except:
        message = f'ERROR: {EXE} -b 1 "{PATH}\\input\\{file}"'
    finally:
        with open('auto_log.log', 'a') as fp:
            fp.write(f'{time.asctime()} :: {message}\n')

try:
    subprocess.check_output(f'{PY} auto_data_extraction.py'.split())
except:
    print('ERROR:', f'{PY} auto_data_extraction.py')
