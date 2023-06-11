def congratulations(pm, tester, *devs):
    print('Happy New Year! Take care of yourself and your loved ones!\nFor:')
    for name in [pm, tester, *devs]:
        print(name)
