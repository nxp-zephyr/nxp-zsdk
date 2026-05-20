# Board Support Status

Zephyr applications are built for hardware platforms targeting specific boards.  NXP actively contributes to the Zephyr Project, enabling Zephyr compatibility for the boards listed below.  To facilitate early customer development, NXP often contributes new board support during the initial phase of this process. As new features, improvements, and bug fixes are developed and implemented, NXP will continue to contribute them to the Zephyr Project.  The status level "All Planned Features" (APF) means all drivers and features NXP plans to support on a platform are released.

NXP leverages an extensive NXP Zephyr downstream ecosystem, see [Introduction to NXP Zephyr Downstream](../Introduction-to-ZSDK-Downstream.md). The downstream board support may include additional features or modifications compared to upstream contributions. Detailed information regarding the current board support is available at:
* NXP Zephyr downstream [NXP boards](https://github.com/nxp-zephyr/nxp-zephyr/tree/main/boards/nxp) and [release notes](https://github.com/nxp-zephyr/nxp-zsdk/tree/main/doc/releases)
* Upstream [NXP boards](https://docs.zephyrproject.org/latest/boards/nxp/index.html) and [release notes](https://docs.zephyrproject.org/latest/releases/index.html#release-notes)

As Zephyr hardware support is board-centric, NXP's release process and support status are also based on individual boards. For those designing custom boards with different System-on-Chip (SoC) part numbers, please refer to NXP's [Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-custom-boards-and-applications/ta-p/2008567).

NXP provides Zephyr support for a wide range of hardware, but the level of maintenance and validation varies by board. Some boards are actively maintained by NXP, prioritized for ongoing development, and continuously tested in NXP's hardware farm. Other boards were contributed by the community, may receive only occasional updates, and are not part of regular test coverage.

To set clear expectations, the Zephyr Project defines [Hardware Support Tiers](https://docs.zephyrproject.org/latest/project/release_process.html#hardware-support-tiers).  These tiers indicate the support commitment, test coverage, and bug‑handling priority for each platform.  The tables below list the current support tier for every board and shield.

NXP is committed to providing comprehensive and high-quality board support for Zephyr.  The following table provides the current status for each supported board:

| NXP Board                         |  Status                                                                              | Board Tier |
|-----------------------------------|--------------------------------------------------------------------------------------|-------------
| frdm_imx91                        | In Development                                                                       |   Tier 1   |
| frdm_imx93                        | In Development                                                                       |   Tier 1   |
| frdm_k22f                         | All Planned Features                                                                 |   Tier 2   |
| frdm_k32l2b3                      | All Planned Features                                                                 |   Tier 2   |
| frdm_k64f                         | All Planned Features                                                                 |   Tier 1   |
| frdm_k82f                         | All Planned Features                                                                 |   Tier 2   |
| frdm_ke15z                        | All Planned Features                                                                 |   Tier 1   |
| frdm_ke16z                        | All Planned Features                                                                 |   Tier 2   |
| frdm_ke17z                        | All Planned Features                                                                 |   Tier 1   |
| frdm_ke17z512                     | All Planned Features                                                                 |   Tier 1   |
| frdm_kl25z                        | All Planned Features                                                                 |   Tier 1   |
| frdm_kw41z                        | All Planned Features                                                                 |   Tier 3   |
| frdm_mcxa153                      | In Development                                                                       |   Tier 1   |
| frdm_mcxa156                      | In Development                                                                       |   Tier 1   |
| frdm_mcxa266                      | In Development                                                                       |   Tier 1   |
| frdm_mcxa344                      | In Development                                                                       |   Tier 1   |
| frdm_mcxa346                      | In Development                                                                       |   Tier 1   |
| frdm_mcxa366                      | In Development                                                                       |   Tier 1   |
| frdm_mcxc242                      | In Development                                                                       |   Tier 1   |
| frdm_mcxc444                      | All Planned Features                                                                 |   Tier 1   |
| frdm_mcxe247                      | In Development                                                                       |   Tier 1   |
| frdm_mcxe31b                      | In Development                                                                       |   Tier 1   |
| frdm_mcxn236                      | In Development                                                                       |   Tier 1   |
| frdm_mcxn947                      | In Development                                                                       |   Tier 1   |
| frdm_mcxw23                       | In Development                                                                       |   Tier 1   |
| frdm_mcxw71                       | All Planned Features                                                                 |   Tier 2   |
| frdm_mcxw72                       | In Development                                                                       |   Tier 1   |
| frdm_rw612                        | All Planned Features                                                                 |   Tier 1   |
| imx8mm_evk                        | All Planned Features                                                                 |   Tier 2   |
| imx8mn_evk                        | All Planned Features                                                                 |   Tier 2   |
| imx8mp_evk                        | All Planned Features                                                                 |   Tier 2   |
| imx8mq_evk                        | All Planned Features                                                                 |   Tier 3   |
| imx8qm_mek                        | All Planned Features                                                                 |   Tier 3   |
| imx8qxp_mek                       | All Planned Features                                                                 |   Tier 3   |
| imx8ulp_evk                       | All Planned Features                                                                 |   Tier 3   |
| imx91_evk                         | In Development                                                                       |   Tier 2   |
| imx91_qsb                         | In Development                                                                       |   Tier 2   |
| imx93_evk                         | In Development                                                                       |   Tier 2   |
| imx943_evk                        | In Development                                                                       |   Tier 2   |
| imx95_evk                         | In Development                                                                       |   Tier 1   |
| imx95_evk_15x15                   | In Development                                                                       |   Tier 2   |
| lpcxpresso11u68                   | All Planned Features                                                                 |   Tier 3   |
| lpcxpresso51u68                   | All Planned Features                                                                 |   Tier 2   |
| lpcxpresso54114                   | All Planned Features                                                                 |   Tier 2   |
| lpcxpresso55s06                   | All Planned Features                                                                 |   Tier 2   |
| lpcxpresso55s16                   | All Planned Features                                                                 |   Tier 2   |
| lpcxpresso55s28                   | All Planned Features                                                                 |   Tier 2   |
| lpcxpresso55s36                   | All Planned Features                                                                 |   Tier 2   |
| lpcxpresso55s69                   | All Planned Features                                                                 |   Tier 1   |
| ls1046ardb                        | All Planned Features                                                                 |   Tier 2   |
| mcx_n5xx_evk                      | In Development                                                                       |   Tier 2   |
| mcx_n9xx_evk                      | In Development                                                                       |   Tier 2   |
| mcxw23_evk                        | In Development                                                                       |   Tier 3   |
| mcxw72_evk                        | In Development                                                                       |   Tier 3   |
| mimxrt1010_evk                    | All Planned Features                                                                 |   Tier 1   |
| mimxrt1015_evk                    | All Planned Features                                                                 |   Tier 2   |
| mimxrt1020_evk                    | All Planned Features                                                                 |   Tier 1   |
| mimxrt1024_evk                    | All Planned Features                                                                 |   Tier 1   |
| mimxrt1040_evk                    | All Planned Features                                                                 |   Tier 1   |
| mimxrt1050_evk                    | All Planned Features                                                                 |   Tier 1   |
| mimxrt1060_evk                    | All Planned Features                                                                 |   Tier 1   |
| mimxrt1062_fmurt6                 | All Planned Features                                                                 |   Tier 2   |
| mimxrt1064_evk                    | All Planned Features                                                                 |   Tier 1   |
| mimxrt1160_evk                    | All Planned Features                                                                 |   Tier 1   |
| mimxrt1170_evk                    | All Planned Features                                                                 |   Tier 1   |
| mimxrt1180_evk                    | In Development                                                                       |   Tier 1   |
| mimxrt595_evk                     | All Planned Features                                                                 |   Tier 1   |
| mimxrt685_evk                     | All Planned Features                                                                 |   Tier 1   |
| mimxrt700_evk                     | In Development                                                                       |   Tier 1   |
| mr_canhubk3                       | All Planned Features                                                                 |   Tier 2   |
| rd_rw612_bga                      | All Planned Features                                                                 |   Tier 2   |
| rddrone_fmuk66                    | All Planned Features                                                                 |   Tier 3   |
| s32k148_evb                       | All Planned Features                                                                 |   Tier 3   |
| s32z2xxdc2                        | All Planned Features                                                                 |   Tier 3   |
| twr_ke18f                         | All Planned Features                                                                 |   Tier 2   |
| twr_kv58f220m                     | All Planned Features                                                                 |   Tier 3   |
| ucans32k1sic                      | All Planned Features                                                                 |   Tier 3   |
| usb_kw24d512                      | All Planned Features                                                                 |   Tier 3   |
| vmu_rt1170                        | All Planned Features                                                                 |   Tier 1   |

Here is the current status and support tier for each NXP [shield](https://docs.zephyrproject.org/latest/hardware/porting/shields.html):

| NXP Shield                        |  Status                                                                              | Board Tier |
|-----------------------------------|--------------------------------------------------------------------------------------|-------------
| frdm_cr20a                        | All Planned Features                                                                 |   Tier 3   |
| frdm_stbc_agm01                   | All Planned Features                                                                 |   Tier 3   |
| g1120b0mipi                       | All Planned Features                                                                 |   Tier 2   |
| lcd_par_s035                      | All Planned Features                                                                 |   Tier 1   |
| nxp_adtja1101                     | All Planned Features                                                                 |   Tier 2   |
| nxp_btb44_ov5640                  | All Planned Features                                                                 |   Tier 1   |
| nxp_m2_wifi_bt using IW416        | All Planned Features                                                                 |   Tier 1   |
| nxp_m2_wifi_bt using IW610        | All Planned Features                                                                 |   Tier 1   |
| nxp_m2_wifi_bt using IW612        | All Planned Features                                                                 |   Tier 1   |
| nxp_s32k5xx_mb                    | All Planned Features                                                                 |   Tier 3   |
| p3t1755dp_ard_i2c                 | All Planned Features                                                                 |   Tier 1   |
| p3t1755dp_ard_i3c                 | All Planned Features                                                                 |   Tier 1   |
| rk043fn02h_ct                     | All Planned Features                                                                 |   Tier 3   |
| rk043fn66hs_ctg                   | All Planned Features                                                                 |   Tier 2   |
| rk055hdmipi4m                     | All Planned Features                                                                 |   Tier 3   |
| rk055hdmipi4ma0                   | All Planned Features                                                                 |   Tier 2   |
| zc143ac72mipi                     | All Planned Features                                                                 |   Tier 1   |
