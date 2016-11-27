import lvappbuilder.act as act
import lvappbuilder.sh as sh
from datetime import datetime

def action_build(variant, debug):
    proj_path = 'Example.lvproj'
    target = 'My Computer'
    build_spec = 'Example'
    version = open('VERSION').read().strip().split('.')
    symbols = {'DEBUG': str(debug).upper()}
    repl_in_file = [ (proj_path, '_VARIANT_', variant) ]
    lv_bits = 32
    log_suffix = variant + '.' + datetime.now().strftime('%Y%m%d%H%M%S')
    build_timeout = 60
    
    act.build(proj_path,
              target,
              build_spec,
              version,
              symbols,
              repl_in_file,
              lv_bits,
              log_suffix,
              build_timeout)
    
def task_build_release():
    """Build release version of the project.
    """
    return {
        'actions': [(action_build, ['Release', False])],
        }

def task_build_debug():
    """Build debug version of the project.
    """
    return {
        'actions': [(action_build, ['Debug', True])],
        }

def task_junk():
    """Created only for clean-up purposes.
    """
    def clean():
        sh.rm('__pycache__')
        sh.rm('build')
        for f in sh.ls('.', r'^.*\.log$'):
            sh.rm(f)
    
    return {
            'actions': [],
            'clean': [clean],
            }