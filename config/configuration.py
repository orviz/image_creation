
registry_cfg = {
    "url" : "docker.io",
    "user": "_put_username",
    "token": "_put_token",
    "images_prefix": "orviz/"
    }

repositories_cfg = {
    "workflow_repository":"https://gitlab.com/dtgeo/workflow-management-system/workflow-registry",
    "software_repository":"/software-catalog/"
    }

build_cfg = {
    "tmp_folder":"/tmp",
    "builder_home": "/image_creation/",
    "base_image": "spack_base",
    "dockerfile": "Dockerfile.spack",
    "spack_cfg":"/software-catalog/cfg",
    "max_concurrent_builds" : 3,
    "singularity_sudo" : True
    }

database = 'sqlite:///db.sqlite'
port = 5000
host = '0.0.0.0'
application_root = 'image_creation'
secret_key = ''
