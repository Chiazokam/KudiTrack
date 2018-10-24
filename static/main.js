//document.getElementById("submit-btn").addEventListener('click', expenseNotification)

function expenseNotification() {
			var expense_date = document.getElementById("expense_date").value;
			var expense_descr = document.getElementById("expense_descr").value;
			var expense_amt = document.getElementById("expense_amt").value;
			var expense_cat = document.getElementById("expense_cat").value;

			$.ajax({
  				url: "http://localhost:5000/addExpense",
  				method: "POST",
          crossDomain : true,
          async: false,
  				data: {
  					"expense_date": expense_date,
  					"expense_amt": expense_amt,
  					"expense_cat": expense_cat,
  					"expense_descr": expense_descr
  				}
  			}).done(function (data) {
  				if (data.expense_amt != '') {
						swal("Good job!", "Expense Added", "success", {
  					button: "Close",
					});
  				}
  				if (!data) {
  					swal({
  						title: "Sorry",
  						text: 'Your Expense has NOT been saved!',
  						type: "error"
  					});
  				}
  			})
				console.log(data)
		}
