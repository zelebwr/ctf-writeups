# This script calculates the CRC-16-MODBUS checksum for a given hexadecimal string.

def calculate_crc(hex_string):
    """
    Calculates the CRC-16-MODBUS for a string of hex bytes.
    
    Args:
        hex_string: A string of hexadecimal values, separated by spaces.
                    Example: "03 04 08 00 1E 00 00 00 00 00 00"
    
    Returns:
        A 16-bit integer representing the CRC checksum.
    """
    # Convert the hex string into a list of integers (byte array)
    data = bytearray.fromhex(hex_string.replace(" ", ""))

    # The CRC calculation starts with a preset value of 0xFFFF
    crc = 0xFFFF
    
    # The polynomial used in Modbus RTU CRC calculation
    polynomial = 0xA001

    # Iterate through each byte of the data
    for byte in data:
        # XOR the current byte with the low byte of the CRC register
        crc ^= byte
        
        # Now, iterate through all 8 bits of the current byte
        for _ in range(8):
            # Check if the least significant bit (LSB) is 1
            if crc & 0x0001:
                # If it is, shift right by one bit
                crc >>= 1
                # And XOR with the polynomial
                crc ^= polynomial
            else:
                # If the LSB is 0, just shift right
                crc >>= 1
    
    return crc

# --- Main execution ---
# Our response packet before the CRC
packet_data = "03 04 08 00 1E 00 00 00 00 00 00"

# Calculate the CRC
crc_value = calculate_crc(packet_data)

# The Modbus protocol requires the CRC to be appended in little-endian format.
# This means the low byte comes first, then the high byte.
low_byte = crc_value & 0xFF
high_byte = (crc_value >> 8) & 0xFF

# Print the results for clarity
print(f"Data for CRC calculation: {packet_data}")
print(f"Calculated CRC (integer): {crc_value}")
print(f"Calculated CRC (hex): {crc_value:04X}")
print(f"Low Byte (hex): {low_byte:02X}")
print(f"High Byte (hex): {high_byte:02X}")
print(f"Final CRC to append (Low Byte, High Byte): {low_byte:02X} {high_byte:02X}")

