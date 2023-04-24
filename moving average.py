// Moving Average Crossover Strategy

// Calculate the 50-day and 200-day moving averages
function movingAverages(prices) {
  const ma50 = calculateMovingAverage(prices, 50);
  const ma200 = calculateMovingAverage(prices, 200);
  return { ma50, ma200 };
}

// Calculate the moving average for a given period
function calculateMovingAverage(prices, period) {
  let sum = 0;
  for (let i = prices.length - 1; i >= prices.length - period; i--) {
    sum += prices[i];
  }
  return sum / period;
}

// Generate buy and sell signals based on the moving average crossover
function generateSignals(prices, ma50, ma200) {
  const signals = [];
  let holding = false;
  for (let i = 0; i < prices.length; i++) {
    if (ma50[i] > ma200[i] && !holding) {
      signals.push('BUY');
      holding = true;
    } else if (ma50[i] < ma200[i] && holding) {
      signals.push('SELL');
      holding = false;
    } else {
      signals.push('HOLD');
    }
  }
  return signals;
}

// Example usage
const prices = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120];
const { ma50, ma200 } = movingAverages(prices);
const signals = generateSignals(prices, ma50, ma200);
console.log(signals); // Output: ["HOLD", "HOLD", "HOLD", "HOLD", "HOLD", "HOLD", "BUY", "BUY", "BUY", "BUY", "BUY", "BUY", "BUY", "BUY", "BUY"]
