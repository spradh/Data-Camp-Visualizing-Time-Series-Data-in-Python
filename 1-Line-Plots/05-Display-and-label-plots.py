# Plot a line chart of the discoveries DataFrame using the specified arguments
ax = discoveries.plot(color = 'blue', figsize = (8, 3), linewidth = 2, fontsize = 6)

# Specify the title in your plot
ax.set_title('Number of great inventions and scientific discoveries from 1860 to 1959', fontsize=8)

# Show plot
plt.show()
