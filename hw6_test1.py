import pytest
import numpy as np

try:
    import field
    import spatial
    import timesteppers
    import equations
except:
    import Week6.field as field
    import Week6.spatial as spatial
    import Week6.timesteppers as timesteppers
    import Week6.equations as equations

# I put my .python files in folders corresponding to the week, so
# don't forget to change that back to whatever you have it to

# CHANGES FROM ORIGINAL: Added 2 tests. The first 1 is shit and supposed to fail.
# The second one should probably pass. Also watch out for the first test from Lecoanet (which is
# the only one this week), I renamed the file in mine, so you might wanna do the same.

error_RD = {(50,0.5):3e-3, (50,0.25):2.5e-3, (50,0.125):2.5e-3,(100,0.5):4e-4, (100,0.25):2e-4, (100,0.125):1e-4, (200,0.5):8e-5, (200,0.25):2e-5, (200,0.125):5e-6}
@pytest.mark.parametrize('resolution', [50, 100, 200])
@pytest.mark.parametrize('alpha', [0.5, 0.25, 0.125])
def test_reaction_diffusion(resolution, alpha):
    grid_x = field.UniformPeriodicGrid(resolution, 20)
    grid_y = field.UniformPeriodicGrid(resolution, 20)
    domain = field.Domain((grid_x, grid_y))
    x, y = domain.values()

    IC = np.exp(-(x+(y-10)**2-14)**2/8)*np.exp(-((x-10)**2+(y-10)**2)/10)

    c = field.Field(domain)
    X = field.FieldSystem([c])
    c.data[:] = IC
    D = 1e-2

    dcdx2 = spatial.FiniteDifferenceUniformGrid(2, 8, c, 0)
    dcdy2 = spatial.FiniteDifferenceUniformGrid(2, 8, c, 1)

    rd_problem = equations.ReactionDiffusion2D(X, D, dcdx2, dcdy2)

    dt = alpha*grid_x.dx

    while rd_problem.t < 1-1e-5:
        rd_problem.step(dt)

    try:
        solution = np.loadtxt('c_%i.dat' % resolution)
    except:
        solution = np.loadtxt('answers2/c_%i.dat' % resolution)

    error = np.max(np.abs(solution - c.data))

    error_est = error_RD[(resolution,alpha)]

    assert error < error_est


# Tests by Richard, don't be sad if they don't pass :(


# WARNING: THIS FIRST TEST IS NOT SUPPOSED TO PASS BUT YOU SHOULD GET AN ERROR THAT LOOKS LIKE
# E       assert (0.6777868832709093, 0.6777868832709093) == (0, 0)
# i.e THE NUMBERS DONT MATTER but you should get an answer at least.
# that being said, if you get an answer significantly different than the one above, LMK

def test_vb():
    resolution=200
    alpha=0.25
    grid_x = field.UniformPeriodicGrid(resolution, 20)
    grid_y = field.UniformPeriodicGrid(resolution, 20)
    domain = field.Domain((grid_x, grid_y))
    x, y = domain.values()

    IC = np.exp(-(x+(y-10)**2-14)**2/8)*np.exp(-((x-10)**2+(y-10)**2)/10)

    u = field.Field(domain)
    v = field.Field(domain)
    X = field.FieldSystem([u,v])
    u.data[:] = IC
    v.data[:] = IC
    nu = 1e-2

    vb_problem = equations.ViscousBurgers2D(X,nu,8)
    dt = alpha*grid_x.dx

    while vb_problem.t < 1-1e-5:
        vb_problem.step(dt)

    error1 = np.max(np.abs(u.data))
    error2 = np.max(np.abs(v.data))

    assert  (error1,error2)==(0,0)


# Ok so this one takes like 2 minutes to run. If it takes too long, reduce n to like 4. Essentially,
# what it does is it checks if your code is really second order in time by varying alpha and then
# comparing your answer to the one with the smallest alpha. I wrote this convinced that my code was wrong
# but then it restored my sanity so...

def test_vb_error():
    n=5
    k=1 # offset
    alpha_list=[1/(2**(i-k)) for i in range(n)]
    big=[]
    for alpha in alpha_list:
        resolution=200

        grid_x = field.UniformPeriodicGrid(resolution, 20)
        grid_y = field.UniformPeriodicGrid(resolution, 20)
        domain = field.Domain((grid_x, grid_y))
        x, y = domain.values()

        IC = np.exp(-(x+(y-10)**2-14)**2/8)*np.exp(-((x-10)**2+(y-10)**2)/10)

        u = field.Field(domain)
        v = field.Field(domain)
        X = field.FieldSystem([u,v])
        u.data[:] = IC
        v.data[:] = IC
        nu = 1e-2

        vb_problem = equations.ViscousBurgers2D(X,nu,8)
        dt = alpha*grid_x.dx

        while vb_problem.t < 1-1e-5:
            vb_problem.step(dt)

        error1 = np.max(np.abs(u.data))
        big.append(error1)
    error=[np.abs(big[i]-big[-1]) for i in range(n)]
    errordiv=[error[i]/error[i+1] for i in range(n-2)]
    print(error)
    print(errordiv)

    assert  min(errordiv)>4
