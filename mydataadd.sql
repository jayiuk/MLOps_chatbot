USE mydata;

INSERT INTO user_log (
    user_pn, int_rate, installment, issue_d_period, debt, cr_line_period, pub_rec, revol_bal,
    revol_util, open_acc, total_acc, mort_acc, collections_12_mths_ex_med, mortgage_debt,
    mortgage_repayment, repayment, mortgage_term
)
VALUES
    ('010-1234-5678', 3.5, 250.0, 18, 10000, 18, 0.0, 5000.0, 45.0, 2, 5, 1, 0.0, 200000, 1500, 1750, 20),
    ('010-2345-6789', 4.2, 320.0, 6, 15000, 5, 1.0, 8000.0, 60.0, 3, 6, 1, 1.0, 250000, 1700, 2020, 25),
    ('010-3456-7890', 2.8, 200.0, 8, 5000, 1, 0.0, 4000.0, 30.0, 1, 4, 0, 0.0, 180000, 1400, 1600, 15),
    ('010-4567-8901', 5.0, 400.0, 7, 20000, 3, 2.0, 10000.0, 70.0, 4, 8, 2, 1.0, 300000, 2000, 2400, 30),
    ('010-5678-9012', 3.7, 270.0, 10, 12000, 5, 0.5, 6000.0, 50.0, 2, 5, 1, 0.0, 220000, 1600, 1900, 20);