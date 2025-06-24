def calculate_thrust(m_dot, v_e, P_e, P_a, A_e):
    """
    Calculate the thrust of a rocket engine.

    Parameters:
    m_dot (float): Mass flow rate (kg/s)
    v_e (float): Exhaust velocity (m/s)
    P_e (float): Exit pressure (Pa)
    P_a (float): Ambient pressure (Pa)
    A_e (float): Nozzle exit area (m^2)

    Returns:
    float: Thrust (N)
    """
    momentum_thrust = m_dot * v_e
    pressure_thrust = (P_e - P_a) * A_e
    total_thrust = momentum_thrust + pressure_thrust
    return total_thrust

# Example values
m_dot = 300     # kg/s
v_e = 2900      # m/s
P_e = 25000     # Pa
P_a = 101000    # Pa
A_e = 1.5       # m^2

# Calculate thrust
thrust = calculate_thrust(m_dot, v_e, P_e, P_a, A_e)
print(f"Thrust: {thrust:.2f} N")
