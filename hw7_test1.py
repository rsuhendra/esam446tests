
import pytest
import numpy as np

try:
    import field
    import spatial
    import timesteppers
    import equations
except:
    import Week7.field as field
    import Week7.spatial as spatial
    import Week7.timesteppers as timesteppers
    import Week7.equations as equations

error_derivative_1 = {(50, 2): 0.005, (100, 2): 0.0015, (200, 2): 4e-4, (50, 4): 4e-5, (100, 4): 2e-6, (200, 4): 1.5e-7, (50, 6): 3e-7, (100, 6): 4e-9, (200, 6): 7e-11}
@pytest.mark.parametrize('resolution', [50, 100, 200])
@pytest.mark.parametrize('convergence_order', [2, 4, 6])
def test_derivative_1(resolution, convergence_order):
    grid = field.UniformNonPeriodicGrid(resolution,(0, 5))
    domain = field.Domain([grid])
    x = grid.values
    u = field.Field(domain, np.sin(x))

    du_op = spatial.FiniteDifferenceUniformGrid(1, convergence_order, u)
    du = du_op.evaluate()

    error = np.max(np.abs(du.data - np.cos(x)))
    error_est = error_derivative_1[(resolution, convergence_order)]

    assert error < error_est

error_diffusion = {(100, 0.5, 2): 2.5e-6, (100, 0.5, 4): 7e-7,   (100, 0.25, 2): 2.5e-6, (100, 0.25, 4): 1.5e-7,
                   (200, 0.5, 2): 6e-7,   (200, 0.5, 4): 1.5e-7, (200, 0.25, 2): 6e-6,   (200, 0.25, 4): 4e-8}
@pytest.mark.parametrize('resolution', [100, 200])
@pytest.mark.parametrize('alpha', [0.5, 0.25])
@pytest.mark.parametrize('spatial_order', [2, 4])
def test_diffusion_equation(resolution, alpha, spatial_order):
    grid_x = field.UniformNonPeriodicGrid(resolution,(0,2*np.pi))
    grid_y = field.UniformPeriodicGrid(resolution,2*np.pi)
    domain = field.Domain([grid_x, grid_y])
    x, y = domain.values()

    c = field.Field(domain)
    X = field.FieldSystem([c])
    D = 1

    r = np.sqrt((x-3*np.pi/4)**2 + (y-np.pi/2)**2)
    IC = np.exp(-r**2*16)
    c.data[:] = IC

    diff = equations.DiffusionBC(X, D, spatial_order)

    dt = alpha*grid_y.dx

    while diff.t < 3*np.pi/4 - 1e-5:
        diff.step(dt)
    try:
        c_target = np.loadtxt('c_%i.dat' %resolution)
    except:
        c_target = np.loadtxt('answers3/c_%i.dat' % resolution)
    error = np.max(np.abs(c.data - c_target))
    error_est = error_diffusion[(resolution, alpha, spatial_order)]

    assert error < error_est


# Richard

error_derivative_2 = {(50, 2): 0.1, (100, 2): 0.05, (200, 2): 0.025, (50, 4): 1e-3, (100, 4): 1.3e-4, (200, 4): 1.6e-5, (50, 6): 1e-5, (100, 6): 3.1e-7, (200, 6): 9.7e-9}
@pytest.mark.parametrize('resolution', [50, 100, 200])
@pytest.mark.parametrize('convergence_order', [2, 4, 6])
def test_derivative_2(resolution, convergence_order):
    grid = field.UniformNonPeriodicGrid(resolution,(0, 5))
    domain = field.Domain([grid])
    x = grid.values
    u = field.Field(domain, np.sin(x))

    du_op = spatial.FiniteDifferenceUniformGrid(2, convergence_order, u)
    du = du_op.evaluate()

    error = np.max(np.abs(du.data +np.sin(x)))
    error_est = error_derivative_2[(resolution, convergence_order)]
    print(error,error_est)
    assert error < error_est