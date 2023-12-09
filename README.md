# Sparerpauschbetrag Optimizer for ETFs

This tool aims to assist you in optimizing your utilization of the 
"Sparerpauschbetrag" by selling shares of your ETF.

:heavy_exclamation_mark: Please note that this tool is provided without any
guarantee. I do not assume any responsibility for the accuracy or completeness
of the results obtained through the use of this tool. The use is at your own
risk, and I disclaim any liability for potential damages or losses that may
arise from the application of this tool. It is recommended to carefully review
the generated results and, if necessary, seek independent professional advice.
The use of this tool implies understanding and agreement with these terms.

The "Sparerpauschbetrag" is a tax-free allowance in Germany designed to exempt
interest income and certain other capital gains from taxation. The term is a
combination of "Sparer" (referring to the investor or saver) and "Pauschbetrag"
(meaning a fixed amount).

Since 2009, Germany has imposed a flat rate withholding tax ("Abgeltungsteuer")
on capital income such as interest, dividends, and capital gains from the sale
of securities. As of 2022, this tax rate is 25 percent, plus a solidarity
surcharge and possibly church tax. The Sparerpauschbetrag serves as an
exemption, allowing a certain amount of capital income to be tax-free.

For singles, the Sparerpauschbetrag is 1000 euros per year, and for married
couples or those in registered civil partnerships, it is 2000 euros per year.
This allowance is independent of the individual's tax rate. If capital income
is below this threshold, it generally does not need to be reported in the
income tax return.

The Sparerpauschbetrag cannot be applied to other types of income, such as
rental income. If capital income exceeds the Sparerpauschbetrag, the excess
amount must be declared and taxed in the income tax return.

It's worth noting that individuals typically don't need to calculate the
remaining Sparerpauschbetrag on their own, as financial institutions
responsible for disbursing capital gains, such as banks and brokerage firms,
usually apply the Sparerpauschbetrag automatically when withholding taxes on
interest and capital gains. However, in cases where multiple financial
institutions are involved or if individuals have various sources of capital
income, they may need to monitor and manage their Sparerpauschbetrag
independently to ensure accurate tax reporting.

In Germany, there is a "partial exemption" for certain capital gains, including
dividends from stocks and returns from investment funds (including ETFs). This
regulation means that only a portion of the capital gains is taken into account
when calculating the capital gains tax.

For private investors, the partial exemption is currently (as of 2022) 30
percent. This implies that only 70 percent of the capital gains from stocks and
investment funds are subject to the capital gains tax. The idea behind this is
to incentivize long-term investments and promote participation in the capital
market.

However, the partial exemption does not apply to all capital gains. For
example, capital gains from the sale of stocks or investment fund shares are
not partially exempt; the full capital gains tax applies in these cases.

It is essential to note that tax regulations are subject to change, and it is
advisable to obtain up-to-date information from a tax advisor or a reliable
source to ensure awareness of the latest provisions.

## How to use

Input all your purchases and sales for a specific fund in the following
format within the files named `0_buys.csv` and `0_sells.csv` (if you do not
have any sells, keep the sells file empty).
```
date, amount, price
2023-12-10, 23, 42.69
```

Call the python script (don't forget to specify your remaining 
"Sparerpauschbetrag" and the current price of the fund you want to sell).

In the following example the remaining "Sparerpauschbetrag" is 834.81€ and the
current price of the fund is 80.95€:
```
python3 main.py 834.81 80.95
```

The script will tell you how many ETF shares you have to sell to optimize the
utilization of your "Sparerpauschbetrag" and what the total will be.
