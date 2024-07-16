import requests, yaml

ip_ranges = requests.get('https://www.cloudflare-cn.com/ips-v4/#').text

data = {
    'payload': []
}

for ip_range in ip_ranges.split('\n'):
    data['payload'].append(ip_range)


class IndentStyle(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(IndentStyle, self).increase_indent(flow, False)


with open("cloudflare.yml", "w") as file:
    yaml.dump(data, file, IndentStyle)
