'''
nose tests for the kiknet api
'''
import kiknet
from itertools import izip


def check_equals_returnsData(M):
    data = kiknet.paramEquals('MwFnet', M, ['gmNo' , 'MwFnet' , 'gmStatus4Components'])
    assert len(data) > 0

def test_equals_returnsData():
    mags = [4.0 , 4.5 , 5.1 , 5.5 , 6.1]
    for mag in mags:
        yield 'check_equals_returnsData', mag

def check_equals_M(M):
    data = kiknet.paramEquals('MwFnet', M, ['gmNo' , 'MwFnet' , 'gmStatus4Components'])
    mags = [ (d['MwFnet'] == M) for d in data]
    mags_999 = [(d['MwFnet'] == -999) for d in data]
    assert all(mags)
    assert not any(mags_999)

def test_equals_M():
    Ms = [4.0 , 4.5 , 5.1 , 5.5 , 6.1]
    for M in Ms:
        yield 'check_equals_M' , M

def check_noiseFilter(M):
    data = kiknet.paramEquals('MwFnet', M, ['gmNo' , 'MwFnet' , 'gmStatus4Components'])
    noiseStatus = [ (d['gmStatus4Components'] == 1) for d in data]
    assert all(noiseStatus)

def test_noiseFilter():
    Ms = [4.0 , 4.5 , 5.1 , 5.5 , 6.1]
    for M in Ms:
        yield 'check_noiseFilter' , M

def check_noiseyData(M):
    '''Test if we get back any noisy results if we switch the noise filter off'''
    data = kiknet.paramEquals('MwFnet', M, ['gmNo' , 'MwFnet' , 'gmStatus4Components'] , False)
    noiseStatus = [ d['gmStatus4Components'] == 0 for d in data]
    assert any(noiseStatus)

def test_noiseyData():
    Ms = [4.0 , 4.5 , 5.1 , 5.5 , 6.1]
    for M in Ms:
        yield 'check_noiseyData', M

def check_paramLessThan(R):
    data = kiknet.paramLessThan('RhypFnetMtDepth', R, ['gmNo' , 'RhypFnetMtDepth'], False)
    Rs = [(d['RhypFnetMtDepth'] < R) for d in data]
    Rs_999 = [d['RhypFnetMtDepth'] == -999 for d in data]
    assert all(Rs)
    assert not any(Rs_999)

def test_paramLessThan():
    Rs = [10 , 50 , 100 , 200 , 300]
    for R in Rs:
        yield 'check_paramLessThan', R

def check_paramGreaterThan(R):
    data = kiknet.paramGreaterThan('RhypFnetMtDepth', R, ['gmNo' , 'RhypFnetMtDepth'], False)
    Rs = [(d['RhypFnetMtDepth'] > R) for d in data]
    Rs_999 = [d['RhypFnetMtDepth'] == -999 for d in data]
    assert all(Rs)
    assert not any(Rs_999)

def test_paramGreaterThan():
    Rs = [10 , 50 , 100 , 200 , 300]
    for R in Rs:
        yield 'check_paramGreaterThan', R

def check_paramLessThanEquals(M):
    data = kiknet.paramLessThanEquals('MwFnet', M, ['gmNo' , 'MwFnet'], False)
    Ms_lessThan = [(d['MwFnet'] <= M) for d in data]
    Ms_equals = [(d['MwFnet'] == M) for d in data]
    Ms_999 = [d['MwFnet'] == -999 for d in data]
    assert all(Ms_lessThan)
    assert any(Ms_equals)
    assert not any(Ms_999)

def test_paramLessThanEquals():
    Ms = [4.5 , 5.5 , 5.7 , 6.5 , 7.5]
    for M in Ms:
        yield 'check_paramLessThanEquals', M

def check_paramGreaterThanEquals(M):
    data = kiknet.paramGreaterThanEquals('MwFnet', M, ['gmNo' , 'MwFnet'], False)
    Ms_greaterThan = [(d['MwFnet'] >= M) for d in data]
    Ms_equals = [(d['MwFnet'] == M) for d in data]
    Ms_999 = [d['MwFnet'] == -999 for d in data]
    assert all(Ms_greaterThan)
    assert any(Ms_equals)
    assert not any(Ms_999)

def test_paramGreaterThanEquals():
    Ms = [4.5 , 5.5 , 5.7 , 6.5 , 7.5]
    for M in Ms:
        yield 'check_paramGreaterThanEquals', M

def check_range_returnsData(mLow , mHigh):
    mRange = '%f to %f' % (mLow , mHigh)
    data = kiknet.paramInRange('MwFnet', mRange, ['gmNo' , 'MwFnet'])
    assert len(data) > 0

def test_range_returnsData():
    mLows = [4.0 , 4.5 , 5.0 , 5.5 , 6.0]
    mHighs = [4.5 , 5.0 , 5.5 , 6.0 , 7]
    for mLow, mHigh in izip(mLows, mHighs):
        yield 'check_range_returnsData' , mLow , mHigh

def check_paramInRange(mLow, mHigh):
    mRange = '%f to %f'% (mLow, mHigh)
    data = kiknet.paramInRange('MwFnet', mRange, ['gmNo' , 'MwFnet'])
    Ms_greaterThan = [d['MwFnet'] > mHigh for d in data]
    Ms_lessThan = [d['MwFnet'] < mLow for d in data]
    Ms_999 = [d['MwFnet'] == -999 for d in data]
    assert not any(Ms_greaterThan)
    assert not any(Ms_lessThan)
    assert not any(Ms_999)

def test_paramInRange():
    mLows = [4.0 , 4.5 , 5.0 , 5.5 , float('-inf')]
    mHighs = [4.5 , 5.0 , float('inf') , 6.0 , 7]
    for mLow, mHigh in izip(mLows, mHighs):
        yield 'check_paramInRange' , mLow , mHigh

def check_multiParamsInRange_returnsData(mLow , mHigh , rLow , rHigh):
    ranges = ['%s to %s' % (mLow , mHigh) , '%s to %s' % (rLow , rHigh)]
    data = kiknet.multiParamsInRange(['MwFnet' , 'RhypFnetMtDepth'] , ranges , ['gmNo' , 'MwFnet' , 'RhypFnetMtDepth'])
    assert len(data) > 0

def test_multiParamsInRange_returnsData():
    rLows = ['0' , '-1' , '50' , '200' , '-inf']
    rHighs = ['10' , '100' , '100' , 'inf' , '100']
    mLows = ['0' , '5', '-inf', '6' , '7']
    mHighs = ['inf' , '6' , '4' ,'7' , '100']
    for mLow , mHigh , rLow , rHigh in izip(mLows , mHighs , rLows , rHighs):
        yield 'check_multiParamsInRange_returnsData' , mLow , mHigh , rLow , rHigh

def check_multiParamsInRange(mLow , mHigh , rLow , rHigh):
    ranges = ['%s to %s' % (mLow, mHigh) , '%s to %s' % (rLow, rHigh)]
    data = kiknet.multiParamsInRange(['MwFnet', 'RhypFnetMtDepth'], ranges, ['gmNo', 'MwFnet', 'RhypFnetMtDepth'])
    ms_lessThan = [d['MwFnet'] < float(mLow) for d in data]
    ms_greaterThan = [d['MwFnet'] > float(mHigh) for d in data]
    rs_lessThan = [d['RhypFnetMtDepth'] < float(rLow) for d in data]
    rs_greaterThan = [d['RhypFnetMtDepth'] > float(rHigh) for d in data]
    ms_999 = [d['MwFnet'] == -999 for d in data]
    rs_999 = [d['RhypFnetMtDepth'] == -999 for d in data]
    assert not any(ms_lessThan)
    assert not any(ms_greaterThan)
    assert not any(rs_lessThan)
    assert not any(rs_greaterThan)
    assert not any(ms_999)
    assert not any(rs_999)

def test_multiParamsInRange():
    rLows = ['0' , '-1' , '50' , '200' , '-inf']
    rHighs = ['10' , '100' , '100' , 'inf' , '100']
    mLows = ['0' , '5', '-inf', '6' , '7']
    mHighs = ['inf' , '6' , '4' ,'7' , '100']
    for mLow, mHigh, rLow, rHigh in izip(mLows, mHighs, rLows, rHighs):
        yield 'check_multiParamsInRange', mLow, mHigh, rLow, rHigh

def checkSpectraForGmNos(gmNos, periods, components):
    data = kiknet.spectraForGmNos(gmNos, periods, components)
    # Check that data is returned
    dataPresent = [len(data[d]) > 0 for d in data]
    assert all(dataPresent)

    # check that name of dict keys are same as component list
    if components == []:
        components = ['MS']
    assert data.keys().sort() == components.sort()
    # check that the number of periods returned is same as requested
    if periods == []:
        periods = [0]*24
    if periods[0] == -1:
        periods = [0]*105
    sameNumberOfPeriods = [len(s)-2 == len(periods) for d in data for s in data[d]]
    assert all(sameNumberOfPeriods)
    # check that the same gmNos are returnes
    returnedGmNos = [[s[0] for s in data[d]] for d in data]
    gmNos.sort()
    sameGmNos = [gm == gmNos for gm in returnedGmNos]
    assert all(sameGmNos)

def testSpectraForGmNos():
    gmNos = [[3] , [3, 4, 5, 6] , [31, 32, 33, 34] , [41, 42] , [45, 46, 47]]
    periods = [[] , [-1, 1] , [1, 2, 3, 4] , [0.01, 1] , [0.05]]
    components = [['MS'], [], ['MS', 'MB'], ['S1', 'S2', 'S3'], ['B1', 'B2', 'B3']]
    for gmNo , per , comp in izip(gmNos, periods, components):
        yield 'checkSpectraForGmNos' , gmNo , per , comp

def testParticularSpectra():
    spectra = kiknet.spectraForGmNos([2] , ['pga', 0.02, 0.03] , ['B1'])
    #print spectra['B1']
    assert spectra['B1'] == [[2, 2, 0.00038584, 0.00039089, 0.00040397]]

    spectra = kiknet.spectraForGmNos([2, 5] , ['pga', 0.02, 0.03] , ['B1'])
    assert spectra['B1'] == [[2, 2, 0.00038584, 0.00039089, 0.00040397] , [5, 7.7778, 0.0021254, 0.0021487, 0.002182]]
