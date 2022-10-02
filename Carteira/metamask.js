import React, {Component} from 'react';
import Web3 from 'web3';

class MetaMaskReactApp extends Component {
    constructor(props) {
        super(props);
        // Create a context object to store the account's address and enable it to be used by any child components
        this.state = {
            accountAddress: ''
        };
        this.handleUnlockMetaMask = this.handleUnlockMetaMask.bind(this);
        this.handleLockMetaMask = this.handleLockMetaMask.bind(this);
    }

    // Detect the presence of MetaMask and see if it's unlocked
    async componentDidMount() {
        // Check if MetaMask is installed
        if (window.ethereum) {
            try {
                // Create a Web3 instance using the ethereum provider provided by MetaMask
                this.web3 = new Web3(window.ethereum);
                // Wait for MetaMask's provider to be ready
                await this.web3.currentProvider.enable();
                // Convert web3 to use the account address exposed by ethereum
                const accounts = await this.web3.eth.getAccounts();
                // Update the context object with the user's account address
                this.setState({accountAddress: accounts[0]});
            } catch (err) {
                // User denied account access...
                console.error(
                    "You need to allow this website to access your Ethereum account. Refreshing..."
                );
            }
        } else {
            // MetaMask is not installed...
            console.error(
                'Oops! It looks like MetaMask is not installed. Refreshing...'
            );
        }
    }

    // Execute the unlockMetaMask function below when the user presses the MetaMask Uninstall button
    // This will attempt to remove MetaMask permanently
    async handleUnlockMetaMask() {
        try {
            await this.web3.currentProvider.request({
                method: 'wallet_getAccounts'
            });
            // The user denied account access
        } catch (err) {
            await this.web3.currentProvider.request({method: 'wallet_lock'});
            // MetaMask has been uninstalled
            this.setState({
                accountAddress: ''
            });
        }
        // Refresh the page if MetaMask is uninstalled
        if (!this.state.accountAddress) {
            window.location.reload(false);
        }
    }

    // Execute the lockMetaMask function below when the user presses the MetaMask Lock button
    // This will attempt to lock MetaMask and sign out the user
    async handleLockMetaMask() {
        try {
            await this.web3.currentProvider.request({method: 'wallet_lock'});
            // MetaMask extension has been locked
        } catch {
            await this.web3.currentProvider.request({method: 'wallet_signout'});
            // MetaMask has been uninstalled
            this.setState({
                accountAddress: ''
            });
        }
        // Refresh the page if MetaMask is uninstalled
        if (!this.state.accountAddress) {
            window.location.reload(false);
        }
    }

    render() {
        return (
            <>
                <div>
                    <h1>MetaMask Extension Controls</h1>
                    {/* If the accountAddress variable is not empty, display the extension controls */}
                    {this.state.accountAddress && (
                        <>
                            {/* If the extension is locked, the user can press the Unlock MetaMask Button */}
                            {!this.state.accountAddress && (
                                <button onClick={this.handleUnlockMetaMask}>
                                    Unlock MetaMask
                                </button>
                            )}
                            {/* If the extension is unlocked, the user can press the Lock MetaMask Button */}
                            {this.state.accountAddress && (
                                <button onClick={this.handleLockMetaMask}>
                                    Lock MetaMask
                                </button>
                            )}
                        </>
                    )}
                    {/* If the accountAddress variable is empty, display a message that MetaMask is not installed */}
                    {!this.state.accountAddress && (
                        <span>
                            Sorry, it looks like MetaMask is not installed. Try
                            refreshing the page.
                        </span>
                    )}
                </div>
            </>
        );
    }
}

export default MetaMaskReactApp;