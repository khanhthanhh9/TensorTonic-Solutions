import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x)
    p = np.array(p)
    expected_value = 0
    # Write code here
    total_prob = np.allclose(np.sum(p), 1, atol=1e-06)
    if not total_prob: 
        raise ValueError
    else :
        expected_value = np.sum(x*p)
    return expected_value
