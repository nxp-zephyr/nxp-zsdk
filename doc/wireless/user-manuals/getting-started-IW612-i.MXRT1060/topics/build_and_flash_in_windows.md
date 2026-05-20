[Index page](../getting-started-iw612-imxrt1060.md) \| [Build and flash examples](build_and_flash_examples.md)

# Build and flash in Windows (CLI)
## Wi-Fi shell example

This section shows how to compile the Wi-Fi shell example.

Step 1 - Command to select NXP IW416\_MURATA-2EL-M2 in Menuconfig. Save the configuration and exit.

```
cd %HOMEPATH%\zephyrproject\zephyr
west build -b mimxrt1060_evk@C samples/net/wifi/shell -d wifi_shell --pristine -DEXTRA_CONF_FILE="nxp/overlay_hosted_mcu.conf;nxp/overlay_debug.conf;nxp/overlay_hostap_hosted_mcu.conf" --shield nxp_m2_2el_wifi_bt -t menuconfig
```

Step 2 - Build the application.

```
west build -b mimxrt1060_evk@C samples/net/wifi/shell -d wifi_shell --pristine -DEXTRA_CONF_FILE="nxp/overlay_hosted_mcu.conf;nxp/overlay_debug.conf;nxp/overlay_hostap_hosted_mcu.conf" --shield nxp_m2_2el_wifi_bt
```

Step 3 - Flash the application.

```
set PATH=%PATH%;C:\nxp\LinkServer_1.5.30 # Change the Linkserver path
west flash --runner linkserver -d wifi_shell
```

**Note:** To run the Wi-Fi shell application, refer to [Wi-Fi shell example](run_wi-fi_shell_example.md).

## Bluetooth shell example

This section shows how to compile the Bluetooth shell example.

Step 1 - Build the application.

```
cd %HOMEPATH%\zephyrproject\zephyr
west build -p always -b mimxrt1060_evk@C --shield nxp_m2_2el_wifi_bt ./tests/bluetooth/shell/ -d IW612_bt_shell
```

Step 2 - Flash the application.

```
set PATH=%PATH%;C:\nxp\LinkServer_1.5.30 (Change the Linkserver path)
west flash --runner linkserver -d IW612_bt_shell
```

**Note:** To run the Bluetooth shell application, refer to [Bluetooth shell example](run_bluetooth_shell_example.md).

## Coexistence shell example

This section shows how to compile the Coexistence shell example.

Step 1 - Modify firmware configuration.

Replace sduart\_nw61x.bin.se to sd\_nw61x.bin.se in %HOMEPATH%/zephyrproject/modules/hal/nxp/zephyr/src/wireless/CMakeLists.txt file.

Step 2 - Build the application.

```
cd %HOMEPATH%\zephyrproject
west build -b mimxrt1060_evk@C --shield nxp_m2_2el_wifi_bt samples/wireless/coex/shell -d coex --pristine -- -DEXTRA_CONF_FILE="overlay-wifi-nxp-hosted-mcu.conf"
```

Step 2 - Flash the application.

```
set PATH=%PATH%;C:\nxp\LinkServer_1.5.30 # Change the Linkserver path
west flash --runner linkserver -d coex
```

**Note:** To run the Coexistence shell application, refer to [Coexistence shell example](run_coexistence_shell_example.md).


**Parent topic:** [Build and flash examples](../topics/build_and_flash_examples.md)
