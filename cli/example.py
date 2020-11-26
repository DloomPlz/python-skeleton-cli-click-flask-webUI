import click
from core import actions


@click.command()
@click.option('--sleep', required=False, default=1, help='Number of Millisecond sleep between detector launch',type=int, multiple=False)
@click.option('--nbcpuid', required=False, default=10, help='Number of CPUID to test', multiple=False, type=int)
@click.option('--nblaunch', required=False, default=100, help='Number of tests to launch', multiple=False, type=int)
@click.option('--virtual', is_flag=True, help='Add this flag if host is virtual', multiple=False)
def LinuxLaunch(sleep, nbcpuid, nblaunch, virtual):
    output = actions.launchTest(sleep, nbcpuid,nblaunch, virtual)
    f = open("result.csv", "a")
    #f.write("Processor, OS Name, OS version, hote Type, nbCpuid, nbLaunch, TimeSleep(ms), Detection Ratio(%)\n")
    f.write(output+"\n")
    f.close()


    