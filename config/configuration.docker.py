
registry_cfg = {
    "url" : "docker.io",
    "user": None,
    "token": None,
    "images_prefix": "orviz/"
    }

repositories_cfg = {
    "workflow_repository":"https://gitlab.com/dtgeo/workflow-management-system/workflow-registry",
    "software_repository":"/software-catalog/"
    }

build_cfg = {
    "tmp_folder":"/tmp",
    "builder_home": "/image_creation/",
    "base_image": "ghcr.io/eflows4hpc/spack_base:0.20.1",
    "dockerfile": "Dockerfile.spack",
    "spack_cfg":"/software-catalog/cfg",
    "max_concurrent_builds" : 3,
    "singularity_sudo" : False
    }

database = 'sqlite:///db.sqlite'
port = 5000
host = '0.0.0.0'
application_root = '/image_creation'
secret_key = '_put_here_the_secret_key'
captcha_web_site_key = None
captcha_site_key = None
