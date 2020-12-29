# LinuxTips64--lsmod

### 功能

用于显示已载入系统的模块

Linux 操作系统的核心具有模块化的特性，因此在编译核心时，务须把全部的功能都放入核心。

您可以将这些功能编译成一个个单独的模块，待需要时再分别载入。

### 语法

```bash
lsmod
```

### 实例

```bash
[root@cxy-centos7-1 ~]# tunctl help
-bash: tunctl: command not found
[root@cxy-centos7-1 ~]# lsmod
Module                  Size  Used by
xt_CHECKSUM            12549  1 
iptable_mangle         12695  1 
ipt_MASQUERADE         12678  3 
nf_nat_masquerade_ipv4    13412  1 ipt_MASQUERADE
iptable_nat            12875  1 
nf_nat_ipv4            14115  1 iptable_nat
nf_nat                 26787  2 nf_nat_ipv4,nf_nat_masquerade_ipv4
tun                    31740  1 
bridge                151336  0 
stp                    12976  1 bridge
llc                    14552  2 stp,bridge
ebtable_filter         12827  0 
ebtables               35009  1 ebtable_filter
devlink                48345  0 
ip6table_filter        12815  0 
ip6_tables             26912  1 ip6table_filter
ipt_REJECT             12541  4 
nf_reject_ipv4         13373  1 ipt_REJECT
nf_conntrack_ipv4      15053  4 
nf_defrag_ipv4         12729  1 nf_conntrack_ipv4
xt_conntrack           12760  3 
nf_conntrack          133095  5 nf_nat,nf_nat_ipv4,xt_conntrack,nf_nat_masquerade_ipv4,nf_conntrack_ipv4
iptable_filter         12810  1 
iosf_mbi               15582  0 
kvm_intel             183621  0 
kvm                   586948  1 kvm_intel
ppdev                  17671  0 
irqbypass              13503  1 kvm
crc32_pclmul           13133  0 
sunrpc                353352  1 
ghash_clmulni_intel    13273  0 
aesni_intel           189414  0 
lrw                    13286  1 aesni_intel
gf128mul               15139  1 lrw
snd_seq_midi           13565  0 
glue_helper            13990  1 aesni_intel
ablk_helper            13597  1 aesni_intel
snd_seq_midi_event     14899  1 snd_seq_midi
cryptd                 21190  3 ghash_clmulni_intel,aesni_intel,ablk_helper
vmw_balloon            18094  0 
pcspkr                 12718  0 
joydev                 17389  0 
snd_ens1371            25076  0 
snd_rawmidi            31294  2 snd_ens1371,snd_seq_midi
snd_ac97_codec        130556  1 snd_ens1371
ac97_bus               12730  1 snd_ac97_codec
snd_seq                62663  2 snd_seq_midi_event,snd_seq_midi
snd_seq_device         14356  3 snd_seq,snd_rawmidi,snd_seq_midi
snd_pcm               105708  2 snd_ac97_codec,snd_ens1371
snd_timer              29912  2 snd_pcm,snd_seq
snd                    83815  7 snd_ac97_codec,snd_timer,snd_pcm,snd_seq,snd_rawmidi,snd_ens1371,snd_seq_device
soundcore              15047  1 snd
sg                     40721  0 
parport_pc             28205  0 
parport                46395  2 ppdev,parport_pc
vmw_vmci               67127  0 
i2c_piix4              22401  0 
ip_tables              27126  3 iptable_filter,iptable_mangle,iptable_nat
xfs                   997127  2 
libcrc32c              12644  3 xfs,nf_nat,nf_conntrack
sd_mod                 46281  3 
crc_t10dif             12912  1 sd_mod
crct10dif_generic      12647  0 
sr_mod                 22416  0 
cdrom                  42556  1 sr_mod
crct10dif_pclmul       14307  1 
crct10dif_common       12595  3 crct10dif_pclmul,crct10dif_generic,crc_t10dif
crc32c_intel           22094  1 
serio_raw              13434  0 
vmwgfx                276430  1 
drm_kms_helper        179394  1 vmwgfx
syscopyarea            12529  1 drm_kms_helper
sysfillrect            12701  1 drm_kms_helper
sysimgblt              12640  1 drm_kms_helper
fb_sys_fops            12703  1 drm_kms_helper
ttm                   114635  1 vmwgfx
drm                   429744  4 ttm,drm_kms_helper,vmwgfx
mptspi                 22628  2 
scsi_transport_spi     30732  1 mptspi
mptscsih               40150  1 mptspi
nfit                   55016  0 
e1000                 137586  0 
libnvdimm             147731  1 nfit
mptbase               106036  2 mptspi,mptscsih
drm_panel_orientation_quirks    12957  1 drm
ata_generic            12923  0 
pata_acpi              13053  0 
ata_piix               35052  0 
libata                243133  3 pata_acpi,ata_generic,ata_piix
dm_mirror              22289  0 
dm_region_hash         20813  1 dm_mirror
dm_log                 18411  2 dm_region_hash,dm_mirror
dm_mod                124407  8 dm_log,dm_mirror
```

