from resource_management import *

class nifi_registry(Script):
    def install(self, env):
        Logger.info("Installing NiFi Registry packages")
        self.install_packages(env)
        Execute('/usr/lib/nifi-registry/bin/nifi-registry.sh install')
        #if any other install steps were needed they can be added here

    def configure(self,env):
        import params
        env.set_params(params)

    #To stop the service, use the linux service stop command and pipe output to log file
    def stop(self, env):
        Logger.info("Stopping NiFi Registry service")
        Execute('service nifi-registry stop')

    #To start the service, use the linux service start command and pipe output to log file
    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        Logger.info("Starting NiFi Reqgistry service")
        Execute('service nifi-registry start')

    #To get status of the, use the linux service status command
    def status(self, env):
        Logger.info("Getting status of NiFi Registry service")
        try:
            Execute('service nifi-registry status')
        except Fail:
            raise ComponentIsNotRunning()

if __name__ == "__main__":
    nifi_registry().execute()
