[Index page](../getting-started-RW612.md) \| [Build and flash examples](build_and_flash_examples.md)

# Build and flash in Windows
## Wi-Fi shell example

This section shows how to compile the Wi-Fi shell example.


Step 1 - Build the application.

Build a Wi-Fi example with embedded supplicant for rd_rw612_bga board.

```
cd %HOMEPATH%\zephyrproject\zephyr
west build -p always -b rd_rw612_bga samples/net/wifi/shell -d wifi -DEXTRA_CONF_FILE="nxp/overlay_rw612.conf"
```

Build a Wi-Fi example with the WPA supplicant for rd_rw612_bga board.

```
cd %HOMEPATH%\zephyrproject\zephyr
west build -p always -b rd_rw612_bga samples/net/wifi/shell -d wifi -DEXTRA_CONF_FILE="nxp/overlay_rw612.conf nxp/overlay_hostap_rw612.conf"
```

Zephyr.bin and zephyr.elf are in the folder: %HOMEPATH%\zephyrproject\zephyr/wifi/zephyr.


Step 2 - Flash the application.

```
west flash -d wifi
```

**Note:** To run the Wi-Fi shell application, refer to [Wi-Fi shell example](run_wi-fi_shell_example.md).

## Bluetooth shell example

This section shows how to compile the Bluetooth shell example.

Step 1 - Build the application.

```
cd %HOMEPATH%\zephyrproject\zephyr
west build -b rd_rw612_bga ./tests/bluetooth/shell/ -d rw612_bt_shell
```

Step 2 - Flash the application.

```
west flash -d rw612_bt_shell
```

**Note:** To run the Bluetooth shell application, refer to [Bluetooth shell example](run_bluetooth_shell_example.md).

## Coexistence shell example

This section shows how to compile the Coexistence shell example.

Step 1 - Build the application.

```
cd %HOMEPATH%\zephyrproject
west build -b rd_rw612_bga samples/wireless/coex/shell -d coex_shell -c -- -DCONF_FILE="prj.conf overlay-wifi-nxp.conf overlay-wifi-nxp-hostap.conf"
```

Step 2 - Flash the application.

```
west flash -d coex_shell
```

**Note:** To run the Coexistence shell application, refer to [Coexistence shell example](run_coexistence_shell_example.md).

**Parent topic:** [Build and flash examples](../topics/build_and_flash_examples.md)
