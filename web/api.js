
const URL = {
  traces: '/api/traces',
  transactions: '/api/transactions'
}

async function fetch(uri, options = {}) {
  if (!options.hasOwnProperty('headers')) {
    options.headers = {}
  }

  options.headers['Accept'] = 'application/json'

  return self.fetch(uri, options)
}

export async function getTraces() {
  let response = await fetch(URL.traces)

  if (response.status < 200 || response.status > 399) {
    throw new Error('Invalid response code: ' + response.status)
  }

  let json = await response.json()

  return json
}

export async function getTrace(id) {
  let response = await fetch(URL.traces + '/' + id)

  if (response.status < 200 || response.status > 399) {
    throw new Error('Invalid response code: ' + response.status)
  }

  let json = await response.json()

  return json
}

export async function getTransactions() {
  let response = await fetch(URL.transactions)

  if (response.status < 200 || response.status > 399) {
    throw new Error('Invalid response code: ' + response.status)
  }

  let json = await response.json()

  return json
}

export async function getTransaction(id) {
  let response = await fetch(URL.transactions + '/' + id)

  if (response.status < 200 || response.status > 399) {
    throw new Error('Invalid response code: ' + response.status)
  }

  let json = await response.json()

  return json
}
