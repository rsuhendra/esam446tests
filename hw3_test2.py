
import pytest
import numpy as np
import Week3.field as field
import Week3.spatial as spatial
import Week3.timesteppers as timesteppers
import time

def pytest_sessionfinish(session, exitstatus):
    reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    duration = time.time() - reporter._sessionstarttime
    reporter.write_sep('=', 'duration: {} seconds'.format(duration), yellow=True, bold=True)

resolution_list = [100, 200, 400]

error_AB_2_2 = {100:0.4, 200:0.15, 400:0.03}
@pytest.mark.parametrize('resolution', resolution_list)
def test_AB_2_2(resolution):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi-2*np.pi*0.2)**2*8)

    d = spatial.FiniteDifferenceUniformGrid(1, 2, grid, stencil_type='centered')

    alpha = 0.4
    ts = timesteppers.AdamsBashforth(u, d, 2, alpha*grid.dx)

    num_periods = 1.8
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_AB_2_2[resolution]

    assert error < error_est

error_AB_2_4 = {100:0.1, 200:0.05, 400:0.01}
@pytest.mark.parametrize('resolution', resolution_list)
def test_AB_2_4(resolution):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi+2*np.pi*0.2)**2*8)

    d = spatial.FiniteDifferenceUniformGrid(1, 4, grid, stencil_type='centered')

    alpha = 0.3
    ts = timesteppers.AdamsBashforth(u, d, 2, alpha*grid.dx)

    num_periods = 1.2
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_AB_2_4[resolution]

    assert error < error_est

error_AB_3_2 = {100:0.5, 200:0.2, 400:0.05}
@pytest.mark.parametrize('resolution', resolution_list)
def test_AB_3_2(resolution):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi-2*np.pi*0.2)**2*8)

    d = spatial.FiniteDifferenceUniformGrid(1, 2, grid, stencil_type='centered')

    alpha = 0.3
    ts = timesteppers.AdamsBashforth(u, d, 3, alpha*grid.dx)

    num_periods = 1.8
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_AB_3_2[resolution]

    assert error < error_est

error_AB_3_4 = {100:0.04, 200:0.002, 400:2e-4}
@pytest.mark.parametrize('resolution', resolution_list)
def test_AB_3_4(resolution):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi+2*np.pi*0.2)**2*8)

    d = spatial.FiniteDifferenceUniformGrid(1, 4, grid, stencil_type='centered')

    alpha = 0.3
    ts = timesteppers.AdamsBashforth(u, d, 3, alpha*grid.dx)

    num_periods = 1.2
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_AB_3_4[resolution]

    assert error < error_est

error_AB_5_4 = {100:0.05, 200:0.003, 400:2e-4}
@pytest.mark.parametrize('resolution', resolution_list)
def test_AB_5_4(resolution):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi-2*np.pi*0.2)**2*8)  

    d = spatial.FiniteDifferenceUniformGrid(1, 4, grid, stencil_type='centered')

    alpha = 0.1
    ts = timesteppers.AdamsBashforth(u, d, 5, alpha*grid.dx)

    num_periods = 1.8
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_AB_5_4[resolution]

    assert error < error_est

error_AB_5_6 = {100:0.003, 200:1.5e-4, 400:4e-5}
@pytest.mark.parametrize('resolution', resolution_list)
def test_AB_5_6(resolution):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values      

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi+2*np.pi*0.2)**2*8)

    d = spatial.FiniteDifferenceUniformGrid(1, 6, grid, stencil_type='centered')

    alpha = 0.1
    ts = timesteppers.AdamsBashforth(u, d, 5, alpha*grid.dx)

    num_periods = 1.2
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_AB_5_6[resolution]

    assert error < error_est

error_AB_6_6 = {100:0.003, 200:6e-5, 400:7e-6}
@pytest.mark.parametrize('resolution', resolution_list)
def test_AB_6_6(resolution):
    grid = field.UniformPeriodicGrid(resolution, 2*np.pi)
    x = grid.values

    IC = np.exp(-(x-np.pi)**2*8)
    u = field.Field(grid, IC)

    target = np.exp(-(x-np.pi+2*np.pi*0.2)**2*8)

    d = spatial.FiniteDifferenceUniformGrid(1, 6, grid, stencil_type='centered')

    alpha = 0.05
    ts = timesteppers.AdamsBashforth(u, d, 6, alpha*grid.dx)

    num_periods = 1.2
    ts.evolve(2*np.pi*num_periods, alpha*grid.dx)

    error = np.max(np.abs( u.data - target))
    error_est = error_AB_6_6[resolution]

    assert error < error_est



