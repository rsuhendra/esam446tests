import pytest
import numpy as np

try:
    import field
    import spatial
    import timesteppers
except:
    import Week4.field as field
    import Week4.spatial as spatial
    import Week4.timesteppers as timesteppers

# I put my .python files in folders corresponding to the week, so
# don't forget to change that back to whatever you have it to

# CHANGES FROM ORIGINAL: Added tests for BFD with non-uniform timesteps. Again, error bound is mostly
# from the original tests, but it should tell you (mostly) if you're doing it right or not

resolution_list = [100, 200, 400]

error_BDF2_wave = {(100,2):0.5, (200,2):0.2, (400,2):0.06, (100,4):0.08, (200,4):0.008, (400,4):0.002}
@pytest.mark.parametrize('resolution', resolution_list)
@pytest.mark.parametrize('spatial_order', [2, 4])
def test_BDF2_wave(resolution, spatial_order):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi-2*np.pi*0.2)**2*8)

    d = spatial.FiniteDifferenceUniformGrid(1, spatial_order, grid, stencil_type='centered')
    
    ts = timesteppers.BackwardDifferentiationFormula(u, d, 2)

    alpha = 0.1
    num_periods = 1.8
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_BDF2_wave[(resolution,spatial_order)]

    assert error < error_est

error_BDF2_diff = {(100,2):2e-3, (200,2):5e-4, (400,2):1.5e-4, (100,4):4e-4, (200,4):1e-4, (400,4):2e-5}
@pytest.mark.parametrize('resolution', resolution_list)
@pytest.mark.parametrize('spatial_order', [2, 4])
def test_BDF2_diff(resolution, spatial_order):
    grid = field.UniformPeriodicGrid(resolution, 50)
    x = grid.values

    IC = np.exp(-(x-20)**2/4)
    u = field.Field(grid, IC)

    target = 1/np.sqrt(5)*np.exp(-(x-20)**2/20)

    d = spatial.FiniteDifferenceUniformGrid(2, spatial_order, grid, stencil_type='centered')

    ts = timesteppers.BackwardDifferentiationFormula(u, d, 2)

    alpha = 0.5
    ts.evolve(4, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_BDF2_diff[(resolution,spatial_order)]

    assert error < error_est

error_BDF3_diff = {(100,2):2e-3, (200,2):5e-4, (400,2):1.5e-4, (100,4):2e-4, (200,4):4e-5, (400,4):1e-5}
@pytest.mark.parametrize('resolution', resolution_list)
@pytest.mark.parametrize('spatial_order', [2, 4])
def test_BDF3_diff(resolution, spatial_order):
    grid = field.UniformPeriodicGrid(resolution, 50)
    x = grid.values

    IC = np.exp(-(x-30)**2/4)
    u = field.Field(grid, IC)

    target = 1/np.sqrt(5)*np.exp(-(x-30)**2/20)

    d = spatial.FiniteDifferenceUniformGrid(2, spatial_order, grid, stencil_type='centered')

    ts = timesteppers.BackwardDifferentiationFormula(u, d, 3)

    alpha = 0.2
    ts.evolve(4, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_BDF3_diff[(resolution,spatial_order)]

    assert error < error_est

error_BDF4_diff = {(100,4):2e-4, (200,4):4e-5, (400,4):1e-5, (100,6):2e-4, (200,6):4e-5, (400,6):1e-5}
@pytest.mark.parametrize('resolution', resolution_list)
@pytest.mark.parametrize('spatial_order', [4, 6])
def test_BDF4_diff(resolution, spatial_order):
    grid = field.UniformPeriodicGrid(resolution, 50)
    x = grid.values

    IC = np.exp(-(x-30)**2/4)
    u = field.Field(grid, IC)

    target = 1/np.sqrt(5)*np.exp(-(x-30)**2/20)

    d = spatial.FiniteDifferenceUniformGrid(2, spatial_order, grid, stencil_type='centered')

    ts = timesteppers.BackwardDifferentiationFormula(u, d, 4)

    alpha = 0.2
    ts.evolve(4, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_BDF4_diff[(resolution,spatial_order)]

    assert error < error_est

error_BDF5_wave = {(100,4):0.04, (200,4):0.006, (400,4):0.001, (100,6):0.02, (200,6):0.005, (400,6):0.001}
@pytest.mark.parametrize('resolution', resolution_list)
@pytest.mark.parametrize('spatial_order', [4, 6])
def test_BDF5_wave(resolution, spatial_order):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi+2*np.pi*0.2)**2*8)

    d = spatial.FiniteDifferenceUniformGrid(1, spatial_order, grid, stencil_type='centered')
    
    ts = timesteppers.BackwardDifferentiationFormula(u, d, 5)

    alpha = 0.5
    num_periods = 1.2
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_BDF5_wave[(resolution,spatial_order)]

    assert error < error_est

error_BDF6_wave = {100:0.02, 200:0.004, 400:0.001}
@pytest.mark.parametrize('resolution', resolution_list)
def test_BDF6_wave(resolution):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi-2*np.pi*0.2)**2*8)

    d = spatial.FiniteDifferenceUniformGrid(1, 6, grid, stencil_type='centered')
    
    ts = timesteppers.BackwardDifferentiationFormula(u, d, 6)

    alpha = 0.5
    num_periods = 1.8
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)
    
    error = np.max(np.abs( u.data - target))
    error_est = error_BDF6_wave[resolution]

    assert error < error_est


# Tests by Richard, don't be sad if they don't pass :(


error_nu_BDF2_diff = {(100,2):2e-3, (200,2):5e-4, (400,2):1.5e-4, (100,4):4e-4, (200,4):1e-4, (400,4):2e-5}
@pytest.mark.parametrize('resolution', resolution_list)
@pytest.mark.parametrize('spatial_order', [2, 4])
def test_nu_BDF2_diff(resolution, spatial_order):
    grid = field.UniformPeriodicGrid(resolution, 50)
    x = grid.values

    IC = np.exp(-(x-20)**2/4)
    u = field.Field(grid, IC)

    target = 1/np.sqrt(5)*np.exp(-(x-20)**2/20)

    d = spatial.FiniteDifferenceUniformGrid(2, spatial_order, grid, stencil_type='centered')

    ts = timesteppers.BackwardDifferentiationFormula(u, d, 2)

    alpha = 0.5
    ts.evolve(2, alpha*grid.dx)
    ts.evolve(4, alpha * grid.dx/2)

    error = np.max(np.abs( u.data - target))
    error_est = error_nu_BDF2_diff[(resolution,spatial_order)]

    assert error < error_est

error_nu_BDF4_diff = {(100,4):2e-4, (200,4):4e-5, (400,4):1e-5, (100,6):2e-4, (200,6):4e-5, (400,6):1e-5}
@pytest.mark.parametrize('resolution', resolution_list)
@pytest.mark.parametrize('spatial_order', [4, 6])
def test_nu_BDF4_diff(resolution, spatial_order):
    grid = field.UniformPeriodicGrid(resolution, 50)
    x = grid.values

    IC = np.exp(-(x-30)**2/4)
    u = field.Field(grid, IC)

    target = 1/np.sqrt(5)*np.exp(-(x-30)**2/20)

    d = spatial.FiniteDifferenceUniformGrid(2, spatial_order, grid, stencil_type='centered')

    ts = timesteppers.BackwardDifferentiationFormula(u, d, 4)

    alpha = 0.2
    ts.evolve(1, alpha * grid.dx/2)
    ts.evolve(3, alpha * grid.dx / 3)
    ts.evolve(4, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_nu_BDF4_diff[(resolution,spatial_order)]

    assert error < error_est


error_nu_BDF5_wave = {(100, 4): 0.04, (200, 4): 0.006, (400, 4): 0.001, (100, 6): 0.02, (200, 6): 0.005, (400, 6): 0.001}
@pytest.mark.parametrize('resolution', resolution_list)
@pytest.mark.parametrize('spatial_order', [4, 6])
def test_nu_BDF5_wave(resolution, spatial_order):
    grid = field.UniformPeriodicGrid(resolution, 2 * np.pi)
    x = grid.values

    IC = np.exp(-(x - np.pi) ** 2 * 8)
    u = field.Field(grid, IC)

    target = np.exp(-(x - np.pi + 2 * np.pi * 0.2) ** 2 * 8)

    d = spatial.FiniteDifferenceUniformGrid(1, spatial_order, grid, stencil_type='centered')

    ts = timesteppers.BackwardDifferentiationFormula(u, d, 5)

    alpha = 0.5
    num_periods = 1.2
    ts.evolve(0.5 * np.pi * num_periods, alpha * grid.dx)
    ts.evolve(1.25 * np.pi * num_periods, alpha * grid.dx/3)
    ts.evolve(2 * np.pi * num_periods, alpha * grid.dx/2)
    error = np.max(np.abs(u.data - target))
    error_est = error_nu_BDF5_wave[(resolution, spatial_order)]

    assert error < error_est