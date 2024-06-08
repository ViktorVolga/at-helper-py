DESCRIPTION = "App for working with directly with modemmanager"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://at-helper.py \
"

S = "${WORKDIR}"

do_install_append () {
    install -d ${D}${bindir}
    install -m 0755 at-helper.py ${D}${bindir}
}

DEPENDS = "python3-pyserial"