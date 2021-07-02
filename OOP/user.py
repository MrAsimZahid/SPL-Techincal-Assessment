class User:
    """
    Base user class
    """
	def __init__(self, firstName, lastName, password, userName):
		self.firstName = firstName
		self.lastName = lastName
		self.password = password
		self.userName = userName
		self.isSignedIn = False
	
	def signin(self, username, password):
        """
        Sign in Method

        return: bool
        """
		if self.userName == username and self.password == password:
			self.isSignedIn = True
			print("signed in")
			return True
		else:
			print("incorrect username/password")
			return False

	def signOut(self):
        """
        Sign out method

        return: bool
        """
		if self.isSignedIn:
			self.isSignedIn = False
			print("signed out")
			return True
		else:
			print("could not sign out/ trying signing in first")
			return False

	def getProfile(self):
        """
        Get user profile
        """
		print("im just an lms user")